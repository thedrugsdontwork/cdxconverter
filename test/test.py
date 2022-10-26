import os
import sys
root="/".join(os.path.abspath(__file__).split("/")[:-2])
print(root)
sys.path.append(root)
from io import StringIO
from cdxconverter.convert import cdx_file_to_mol
from rdkit.Chem import Draw
from rdkit import Chem
import time
if __name__=='__main__':
    file = "./target.cdx"
    lis=cdx_file_to_mol(file)
    rmol=lis[0].GetMol()
    with open("./test.mol", "wt", encoding="utf-8") as fp:
        fp.write(Chem.MolToMolBlock(rmol))
    mol=Chem.MolFromMolFile("./test.mol")
    # time.sleep(1)
    Draw.MolToFile(rmol, "./test.png",size=(500,500))

    with open("./test.smiles","wt",encoding="utf-8") as fp:
        fp.write(Chem.MolToSmiles(mol))

    print(Chem.MolToMolBlock(mol))
    print(Chem.MolToSmiles(mol))
    targetMol=Chem.MolFromMolFile("./target.mol")
    print(f"{Chem.MolToSmiles(mol)}=={Chem.MolToSmiles(targetMol)}:{Chem.MolToSmiles(mol)==Chem.MolToSmiles(targetMol)}")
