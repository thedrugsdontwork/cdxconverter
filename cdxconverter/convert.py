import sys
import json
# from rdkit import Chem
from rdkit.Geometry import Point3D,Point2D
# from rdkit.Chem import AllChem
from .parser  import cdx_reader
import traceback
from rdkit.Chem.rdchem import RWMol,BondDir,BondStereo,BondType,Conformer,StereoGroupType,Atom, Bond, Mol
from .enumconverter import *
import logging
from rdkit.Chem.rdchem import StereoGroup
from rdkit.Chem import rdmolops ,rdDepictor
LOG=logging.getLogger(__name__)
LOG.addHandler(
    logging.StreamHandler(
        sys.stdout
    )
)
LOG.setLevel(
    logging.DEBUG
)
BOND_TYPE={
    1   : BondType.SINGLE,
    2   : BondType.DOUBLE,
    4   : BondType.TRIPLE,
    8   : BondType.QUADRUPLE,
    0x80: BondType.AROMATIC
}

STEREO_TYPE={
    0   : 'Unspecified',
    1   : 'None'	,
    2   : 'Absolute'	,
    3   : 'Or',#	Or (requires kCDXProp_Atom_EnhancedStereoGroupNum)
    4   : 'And'#	And
}
NODE_TYPE={
    0   : 'Unspecified',
	1   : 'Element',
	2   : 'ElementList',
	3   : 'ElementListNickname',
	4   : 'Nickname',
    5   : 'Fragment',
    6   : 'Formula',
	7   : 'GenericNickname',
	8   : 'AnonymousAlternativeGroup',
	9   : 'NamedAlternativeGroup',
	10  : 'MultiAttachment',
    11  : 'VariableAttachment',
	12  : 'ExternalConnectionPoint',
    13  : 'LinkNode'
}
def convertJson2Mol(data:dict,sanitize=False,removeHs=False):
    ids             = dict()
    mols            = list()
    fragment_lookup = dict()
    missing_frag_id = -1
    for key in data:
        #top_level prop
        #filter top_level other props  
        if key=="Page" :
            LOG.info("Start parse page")
            page=data[key]
            for item in page:
                for p_key in item:
                    if p_key == "Fragment":
                        LOG.info("Start parse fragment")
                        
                        for frag in item[p_key]:
                            rmol = RWMol()
                            if not parse_fragment(rmol, frag, ids, missing_frag_id):
                                continue
                            frag_id = rmol.GetIntProp("CDX_FRAG_ID")
                            fragment_lookup[frag_id] = len(mols)
                            # if (rmol.HasProp("CDX_NEEDS_FUSE")):
                                # rmol.ClearProp("CDX_NEEDS_FUSE")
                                # std::unique_ptr<ROMol> fused;
                                # try :
                                # fused = std::move(molzip(*mol, molzip_params))
                                    # except Exception as e: (Invar::Invariant &) {
                                    # BOOST_LOG(rdWarningLog)
                                    #     << "Failed fusion of fragment skipping... " << frag_id
                                    #     << std::endl;
                                    # // perhaps have an option to extract all fragments?
                                    # // mols.push_back(std::move(mol));
                                    # continue;
                                    # }
                                # fused.SetIntProp("CDX_FRAG_ID", frag_id)
                                # mols.append(dynamic_cast<RWMol *>(fused.release()));
                            # else :
                                # mols.append(rmol)
                            mols.append(rmol)
                            res     = mols[-1]
                            conf    = Conformer(res.GetNumAtoms())
                            conf.Set3D(False)
                            hasConf = False
                            for atm in res.GetAtoms():
                                if atm.HasProp("CDX_ATOM_POS"):
                                    hasConf = True
                                    coord   = json.loads(atm.GetProp("CDX_ATOM_POS"))
                                    p       = Point3D()
                                    if(len(coord) == 2):
                                        p.x = coord['x']
                                        p.y = coord['y']
                                        p.z = coord.get('z',0.0)
                                    # LOG.debug(f"Set position {atm.GetIdx()} {coord}")
                                    conf.SetAtomPosition(atm.GetIdx(), p)
                                    atm.ClearProp("CDX_ATOM_POS")
                            if (hasConf) :
                                confidx = res.AddConformer(conf)
                                # rdmolops.AssignChiralTypesFromBondDirs(res,res.GetConformer(confidx))
                                # rdmolops.DetectAtomStereoChemistry(res, res.GetConformer(confidx));
                            # func arg
                            if (sanitize):
                                try :
                                    if (removeHs) :
                                        rdmolops.RemoveHs(res,False,False)
                                    else:
                                        rdmolops.SanitizeMol(res)
                                except Exception as e :
                                    LOG.error(f"CDXMLParser: failed sanitizing skipping fragment {frag_id} ")
                                    mols.pop(-1)
                                    continue

                                # // now that atom stereochem has been perceived, the wedging
                                # // information is no longer needed, so we clear
                                # // single bond dir flags:

                                # ClearSingleBondDirFlags(*res)
                                rdmolops.DetectBondStereochemistry(res)
                                rdmolops.AssignStereochemistry(res, True, True, True)
                            else :
                                # ClearSingleBondDirFlags(*res)
                                rdmolops.DetectBondStereochemistry(res)
                            
                
    return mols
                    
                    
                    


def parse_fragment(mol,frag, ids, missing_frag_id,external_attachment=-1):
    # default -1 unknown
    frag_id = frag.get("id",-1)
    if frag_id==-1:
        LOG.warning("Invalid or missing fragment id from CDXML fragment, assigning new one...")
        frag_id = missing_frag_id
        missing_frag_id -= 1
    mol.SetIntProp("CDX_FRAG_ID", frag_id)
    atom_id = -1
    # std::vector<BondInfo> bonds;
    # std::map<int, StereoGroupInfo> sgroups;
    sgroups         =dict()
    bonds           =[]
    skip_fragment   =False
    for node in frag.get("Node",[]):
        elemno          = 6         # default to carbon
        num_hydrogens   = 0
        charge          = 0
        atommap         = 0
        mergeparent     = -1
        rgroup_num      = -1
        isotope         = 0
        sgroup          = -1
        explicitHs      = False
        grouptype       = StereoGroupType.STEREO_ABSOLUTE
        query_label     = ""
        bond_ordering   = []
        elementlist     = []
        atom_coords     = []
        nodetype        = ""
        for attr in node:
            #get attr
            if attr == "id" :
                atom_id = node[attr]
                if (ids.get(atom_id)):#duplicated
                    LOG.error( f"Warning, duplicated atom id {atom_id} skipping fragment" )
                    skip_fragment = True
                    break
            elif attr=="Node_Element":
                #atom index number
                if elemno==6:#change it when elemno is default value
                    elemno=node[attr]
            elif attr== "Atom_NumHydrogens":
                #H number
                num_hydrogens = node[attr]
                explicitHs = True
            elif attr== "Atom_Charge":
                #Atom Charge number

                charge = node[attr]
                LOG.debug(f"get charge {charge}")
            elif attr== "Atom_Isotope":
                #if not contained The atom is assumed to be of natural abundance
              isotope = node[attr]
            elif (attr== "Node_Type") :

                #if not contain default atom
                nodetype = NODE_TYPE.get(node[attr],'Unspecified')
                if (nodetype == "Nickname" or nodetype == "Fragment"):     
                    elemno  = 0
                    atommap = atom_id
                elif (nodetype == "ExternalConnectionPoint"):
                    if (external_attachment <= 0):
                        LOG.error("External Connection Point is not set skipping fragment")
                        skip_fragment = True
                        break
                    
                    elemno  = 0
                    atommap = external_attachment
                    mergeparent = external_attachment
                elif (nodetype == "GenericNickname"):
                    # http://www.cambridgesoft.com/services/documentation/sdk/chemdraw/cdx/properties/Node_Type.htm
                    LOG.warning("Some produce is ignore.......")
                    elemno = 0
                    ##pass this produce is not correct
                elif nodetype == "ElementList":
                    query_label = "ElementList"
                elif nodetype=="Unspecified":
                    elemno = 0
                # LOG.debug(f"Now Atom is {elemno},{nodetype},{node[attr]}")
            elif attr=="Atom_ElementList":
                elementlist = node[attr]
            elif attr== "2DPosition":
                atom_coords = node[attr]
            # elif attr== "3DPosition":
            # # 暂不知晓rdkit对3d分子如何处理，这里暂不做处理，只使用2d坐标
            #     atom_coords = node[attr]
            elif attr == "Atom_EnhancedStereoGroupNum":
                #uint16
                sgroup = node[attr]
            elif (attr == "Atom_EnhancedStereoType") :
                # uint8
                stereo_type = STEREO_TYPE.get(node[attr],0)
                if (stereo_type == "And"):
                    grouptype = StereoGroupType.STEREO_AND
                elif (stereo_type == "Or"):
                    grouptype = StereoGroupType.STEREO_OR
                elif (stereo_type == "Absolute"):
                    grouptype = StereoGroupType.STEREO_ABSOLUTE
                else:
                    LOG.warning(f"Unhandled enhanced stereo type {stereo_type} ignoring")
        # CHECK_INVARIANT(atom_id != -1, "Uninitialized atom id in cdxml.")
        atom = Atom(elemno)
        atom.SetFormalCharge(charge)
        atom.SetNumExplicitHs(num_hydrogens)
        atom.SetNoImplicit(explicitHs)
        atom.SetIsotope(isotope)
        if (rgroup_num >= 0) :
            atom.SetAtomMapNum(rgroup_num)
        # set_fuse_label(rd_atom, atommap);
        if (mergeparent > 0):
            atom.SetIntProp("MergeParent", mergeparent)
        atom.SetProp("CDX_ATOM_POS", json.dumps(atom_coords))#position
        atom.SetUnsignedProp("CDX_ATOM_ID", atom_id)
        updateLabels    = True
        takeOwnership   = True
        idx             = mol.AddAtom(atom)#, updateLabels, takeOwnership)
        
        #关于query的设置暂时先搁置
        # if len(query_label)>0:
        #     if (query_label[0] == 'R'):
        #         atom = addquery(makeAtomNullQuery(), query_label, mol, idx);
        #     elif (query_label == "A"):
        #         atom = addquery(makeAAtomQuery(), query_label, mol, idx);
        #     elif (query_label == "Q"):
        #         atom = addquery(makeQAtomQuery(), query_label, mol, idx);
        #     elif (query_label == "ElementList"):
        #         if len(elementlistz)==0:
        #             LOG.warning("ElementList is empty, ignoring...")
        #         else:
        #             q = new ATOM_OR_QUERY;
        #                 q.SetDescription("AtomOr");
        #             for atNum in elementlist :
        #                 q.addChild(QueryAtom::QUERYATOM_QUERY::CHILD_TYPE(
        #                 makeAtomNumQuery(atNum)));
                    
        #             atom = addquery(q, query_label, mol, idx);
        #             atom.setAtomicNum(elementlist.front());
        #     else :
        #         atom.setProp(common_properties::atomLabel, query_label);
        #stereo 设置估计也得搁置
        if sgroup != -1 :
            stereo = sgroups[sgroup]
            if (stereo.sgroup != -1 and stereo.grouptype != grouptype) :
                LOG.warning("StereoGroup has conflicting stereo group types, ignoring")
                stereo.conflictingSgroupTypes = True
            stereo.grouptype = grouptype
            stereo.atoms.append(atom)
        ###end of stereo
        ids[atom_id]=idx
        if (nodetype == "Nickname" or nodetype == "Fragment"):

            for attr_2 in node :
                if (attr_2 == "fragment"):
                    if (not parse_fragment(mol, node[attr_2], ids, missing_frag_id,
                                        atom_id)):
                        skip_fragment = True
                        break
                    
                    mol.SetBoolProp("CDX_NEEDS_FUSE", True)
                    # // might need to reset to OUR frag_id since parse_fragment will set
                    # //  it to the fragments
                    mol.setProp("CDX_FRAG_ID", frag_id)
        
    for bond in frag.get("Bond",[]):
        bond_id     = -1
        start_atom  = -1
        end_atom    = -1
        order       = BondType.SINGLE
        display     = "Solid"
        for attr in bond:
            try :
                if attr == "id":
                    bond_id     = bond[attr]
                elif attr == "Bond_Begin": 
                    start_atom  = bond[attr]
                elif (attr == "Bond_End"):
                    end_atom    = bond[attr]
                elif (attr == "Bond_Order"):
                    bond_order  = bond[attr]

                    order=BOND_TYPE.get(bond_order,None)
                    if order ==None:
                        LOG.warning("Unhandled bond order set default single")
                        order   = BOND_TYPE.get(1)
                elif (attr =="Bond_Display"):
                    #// gets wedge/hash stuff and probably more
                    display = BOND_DISPLAY.get(bond[attr],'Solid')
            except Exception as e: 
                traceback.print_exc()
                LOG.error(e.args)
                LOG.error(f"Failed to parse cdx fragment node: {bond} attribute:{attr} val:{bond[attr]}")
                return False
        # bond_info=bond{bond_id, start_atom, end_atom, order, display};
        # BondInfo bond{bond_id, start_atom, end_atom, order, display};
        bonds.append((bond_id, start_atom, end_atom, order, display))

    if (not skip_fragment) :
        for bond in bonds:
            # unsigned int bond_idx;
            bond_id     = bond[0]
            bond_end    = bond[2]
            bond_begin  = bond[1]
            bond_type   = bond[3]
            bond_display= bond[4]
            if (bond_display == "WedgeEnd" or bond_display == "WedgedHashEnd") :
                # // here The "END" of the bond is really our Beginning.
                # // swap atom direction
                bond_idx = mol.AddBond(ids[bond_end],ids[bond_begin],bond_type)-1
            else:
                bond_idx = mol.AddBond(ids[bond_begin],ids[bond_end],bond_type)-1
        
            bnd = mol.GetBondWithIdx(bond_idx)
            if (bond_type ==BondType.AROMATIC):
                LOG.info(f"This bond is Aromati")
                bnd.SetIsAromatic(True)
                ids[bond_end].SetIsAromatic(True)
                ids[bond_begin].SetIsAromatic(True)
            
            bnd.SetIntProp("CDX_BOND_ID",bond_id)
            # // More confusion
            # // RDKit/MolFile Wedge (up)  == CDXML WedgedHash
            # // RDKit//MolFile WedgedHash (down) == CDXML Wedge
            if (bond_display == "WedgeEnd" or bond_display == "WedgeBegin") :
                # bnd.SetBondDir(BondDir.BEGINDASH)
                bnd.SetBondDir(BondDir.BEGINWEDGE)
            elif (bond_display == "WedgedHashBegin" or bond_display == "WedgedHashEnd"):
                # bnd.SetBondDir(BondDir.BEGINWEDGE)
                bnd.SetBondDir(BondDir.BEGINDASH)

    #忽略这里先
    # if len(sgroups)>0:
    #     # std::vector<StereoGroup> stereo_groups;
    #     stereo_groups=[]
    #     for sgroup in  sgroups:
    #         stereo_groups.append(StereoGroup(sgroup.second.grouptype, sgroup.second.atoms))
    #     mol.SetStereoGroups(stereo_groups)
    
    return not skip_fragment
            
          
            
      
            
      
def cdx_file_to_mol(file)->list:
    cdx_obj = cdx_reader(file)
    lis = convertJson2Mol(cdx_obj)
    return lis

            
                
                
if __name__=="__main__":
    file = ""
    lis=cdx_file_to_mol(file)
    rmol=lis[0].GetMol()