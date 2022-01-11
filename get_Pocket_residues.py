#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jan 11 16:37:31 2022

@ author: Yu Zhu

@ Email: yzhu99@stu.suda.edu.cn

@ Address: Center for Systems Biology, Department of Bioinformatics, School of Biology and Basic Medical Sciences, Soochow University, Suzhou 215123, China.

"""

### Introduction of get_Pocket_residues.py
#
# @ This part of program is delicated for getting pocket residues from Fpocket outputs.
# @ Reference: Le Guilloux V, Schmidtke P, Tuffery P. Fpocket: an open source platform for ligand pocket detection. BMC Bioinformatics. 2009;10:168. Published 2009 Jun 2.
#
# @ Python package in need: os, argparse, pandas
#
# @ Usage:
#   python get_Pocket_residues.py -path ./test_out
#
#############################################


import os
import pandas as pd
import argparse


parser = argparse.ArgumentParser(description = 'A tool for getting pocket residues from Fpocket outputs.')
parser.add_argument('-path', action = "store", dest = "directory", help = "The directory of Fpocket output folder (named with _out as a tail).")

arg = parser.parse_args()
os.chdir(arg.directory)


# Check the path of Fpocket outputs folder.
def check_path(path):
    
    flag = False
    
    if path.endswith("_out"):
        os.chdir("./pockets")
        flag = True
        print("\n *** Path has been changed to pockets folder. *** \n")
    
    elif path.endswith("pockets"):
        flag = True
        print("\n *** Path has already been in pockets folder. *** \n")
        
    else:
        print("\n *** Please check the path! *** \n")

    return flag


# Get pocket residues from one pdb file.
# Return a dictionary whose keys are chain identifiers and values are residues. 
def find_pocket_residues_from_pdb(pdb_file):
    
    with open(pdb_file, 'r+') as input_pdb:
        lines = input_pdb.readlines()
    
    residues = []
    chains = []
    
    for line in lines:
        if line.startswith('ATOM'):
            resname = line[17:20].strip()
            resnum = line[23:26].strip()        
            chain = line[21].strip()
            chains.append(chain)
            residue = chain + "_" + resname + str(resnum)        
            residues.append(residue)        
    
    chains = list(set(chains)) 
    
    chain_residue = {}
    
    for chain in chains:
        chain_residue[chain] = []
    
        for residue in residues:
            if residue.startswith(chain):
                chain_residue[chain].append(residue[2:])
        
    return chain_residue


path = os.path.abspath(".")

if check_path(path):
    
    files = os.listdir()
    df = pd.DataFrame(columns = ["Fpocket_Number", "Chain_Residues"])
        
    for file in files:
        if file.endswith(".pdb"):
            pocket_number = file.split("_")[0]
            
            temp_dic = find_pocket_residues_from_pdb(file)
            
            df.loc[pocket_number] = [pocket_number, temp_dic]
    
    df.sort_index().to_csv("Fpockets_residues.csv", sep = "\t", index = False)
    
    print("\n *** Jobs Done! *** \n")

else:
    
    print("\n *** Invalid input! *** \n")

