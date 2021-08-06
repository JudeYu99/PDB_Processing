# -*- coding: utf-8 -*-
# @Author: chnzhuyu
# @Date:   2021-08-03 17:24:00
# @Last Modified by:   chnzhuyu
# @Last Modified time: 2021-08-06 15:48:20

## Usage:
#   python ATOM_add.py -f protein.pdb -add 100 > processed.pdb
##

import argparse

parser = argparse.ArgumentParser(description='A tool for quickly adding residue (ATOM) index in pdb files.')
parser.add_argument('-f', action = "store", dest = "filename", help = "PDB File Name")
parser.add_argument('-n', action = "store", dest = "number", help = "original number for the first residue (ATOM) in the input pdb file", type = int, default = 0)
parser.add_argument('-add', action = "store", dest = "addnumber", help = "the number to be added for all residues (ATOM)", type = int, default = 0)
parser.add_argument('-chain', action = "store", dest = "chain", help = "the chain for adding number and default for all chains", type = str, default = "A")

arg = parser.parse_args()

input_pdb = open(arg.filename, 'r')

all_chains = []
chain_flag = True

for lines in input_pdb:
    # chain indentifier
    chain = lines[21].strip()
    all_chains.append(chain)
    
    if lines.startswith('ATOM') or lines.startswith('HETATM'):
        serial = lines[6:11].strip()
        num = lines[22:26].strip()

        if arg.chain not in set(all_chains):
            chain_flag = False
        
        if chain == arg.chain:
            if int(num) >= arg.number:
                print(lines[:22] + str(int(num) + arg.addnumber).rjust(4) + lines[26:], end = '')
            else:
                print(lines, end = '')
        else:
            pass

    else:
        print(lines, end = '')

if chain_flag == False:
    print("Invalid chain identifier!")


