import os
import sys
root="/".join(os.path.abspath(__file__).split("/")[:-2])
print(root)
sys.path.append(root)
from io import StringIO
from cdxconverter.convert import cdx_file_to_mol
from cdxconverter.parser import cdx_reader
from rdkit.Chem import Draw
from rdkit import Chem
import time
import json
if __name__=='__main__':
    file = "./test.cdx"
    data=cdx_reader(file)
    lis=cdx_file_to_mol(file)
    print(len(lis))
    counter=0
    for i in lis:
        rmol=i.GetMol()
    # with open("/Users/yaojunhao/downloads/W2结构/HX-4.mol", "wt", encoding="utf-8") as fp:
    #     fp.write(Chem.MolToMolBlock(rmol))
    # mol=Chem.MolFromMolFile("./test.mol")
    # time.sleep(1)
        Draw.MolToFile(rmol, f"./test{counter}.png",size=(1000,1000))
        with open(f"./test{counter}.mol","wt",encoding="utf-8") as fp:
            fp.write(Chem.MolToMolBlock(rmol))
        counter+=1

    # print(Chem.MolToMolBlock(mol))
    # print(Chem.MolToSmiles(mol))
    # targetMol=Chem.MolFromMolFile("./target.mol")
    # print(f"{Chem.MolToSmiles(mol)}=={Chem.MolToSmiles(targetMol)}:{Chem.MolToSmiles(mol)==Chem.MolToSmiles(targetMol)}")
