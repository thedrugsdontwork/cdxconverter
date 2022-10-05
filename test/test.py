from io import StringIO
from cdxconverter.convert import cdx_file_to_mol
from rdkit.Chem import Draw
from rdkit import Chem
if __name__=='__main__':
    file = "./target.cdx"
    lis=cdx_file_to_mol(file)
    rmol=lis[0].GetMol()
    with open("./test.mol", "wt", encoding="utf-8") as fp:
        fp.write(Chem.MolToMolBlock(rmol))
    mol=Chem.MolFromMolFile("./test.mol")

    Draw.MolToFile(mol, "./test.png",size=(300,300))

    with open("./test.smiles","wt",encoding="utf-8") as fp:
        fp.write(Chem.MolToSmiles(mol))

    print(Chem.MolToMolBlock(mol))
    print(Chem.MolToSmiles(mol))
    targetMol=Chem.MolFromMolFile("./target.mol")
    print(f"Chem.MolToSmiles(mol)==Chem.MolToSmiles(targetMol):{Chem.MolToSmiles(mol)==Chem.MolToSmiles(targetMol)}")