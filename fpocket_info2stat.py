# -*- coding: utf-8 -*-
# @Author: Yu Zhu
# @Email: yzhu99@stu.suda.edu.cn

## Usage:
#   python fpocket_info2stat.py -f protein_info.txt
##

import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='A tool for quickly converting fpocket output file (*_info.txt) to statistical csv files.')
parser.add_argument('-f', action = "store", dest = "filename", help = "info.txt File Name")
arg = parser.parse_args()

def info2stat(arg.filename):

    with open(filename, "r+") as info:
        lines = info.readlines()

        pockets = []
        Score = []
        Druggability_Score = []
        Number_of_Alpha_Spheres = []
        Total_SASA = []
        Polar_SASA = []
        Apolar_SASA = []
        Volume = []
        Mean_local_hydrophobic_density = []
        Mean_alpha_sphere_radius = []
        Mean_alp_sph_solvent_access = []
        Apolar_alpha_sphere_proportion = []
        Hydrophobicity_score = []
        Volume_score = []
        Polarity_score = []
        Charge_score = []
        Proportion_of_polar_atoms = []
        Alpha_sphere_density = []
        Cent_of_mass_Alpha_Sphere_max_dist = []
        Flexibility = []

        for pocket in lines:
            if pocket.startswith("Pocket"):
                pockets.append(pocket.split(" :")[0])
            elif pocket.startswith("\tScore"):
                Score.append(pocket.split("Score : \t")[1].strip())
            elif pocket.startswith("\tDruggability Score"):
                Druggability_Score.append(pocket.split("Druggability Score : \t")[1].strip())
            elif pocket.startswith("\tNumber of Alpha Spheres"):
                Number_of_Alpha_Spheres.append(pocket.split("Number of Alpha Spheres : \t")[1].strip())
            elif pocket.startswith("\tTotal SASA"):
                Total_SASA.append(pocket.split("Total SASA : \t")[1].strip())
            elif pocket.startswith("\tPolar SASA"):
                Polar_SASA.append(pocket.split("Polar SASA : \t")[1].strip())
            elif pocket.startswith("\tApolar SASA"):
                Apolar_SASA.append(pocket.split("Apolar SASA : \t")[1].strip())
            elif pocket.startswith("\tVolume :"):
                Volume.append(pocket.split("Volume : \t")[1].strip())
            elif pocket.startswith("\tMean local hydrophobic density"):
                Mean_local_hydrophobic_density.append(pocket.split("Mean local hydrophobic density : \t")[1].strip())
            elif pocket.startswith("\tMean alpha sphere radius"):
                Mean_alpha_sphere_radius.append(pocket.split("Mean alpha sphere radius :\t")[1].strip())
            elif pocket.startswith("\tMean alp. sph. solvent access"):
                Mean_alp_sph_solvent_access.append(pocket.split("Mean alp. sph. solvent access : \t")[1].strip())
            elif pocket.startswith("\tApolar alpha sphere proportion"):
                Apolar_alpha_sphere_proportion.append(pocket.split("Apolar alpha sphere proportion : \t")[1].strip())
            elif pocket.startswith("\tHydrophobicity score"):
                Hydrophobicity_score.append(pocket.split("Hydrophobicity score:\t")[1].strip())
            elif pocket.startswith("\tVolume score"):
                Volume_score.append(pocket.split("Volume score: \t")[1].strip())
            elif pocket.startswith("\tPolarity score"):
                Polarity_score.append(pocket.split("Polarity score:\t")[1].strip())
            elif pocket.startswith("\tCharge score"):
                Charge_score.append(pocket.split("Charge score :\t")[1].strip())
            elif pocket.startswith("\tProportion of polar atoms"):
                Proportion_of_polar_atoms.append(pocket.split("Proportion of polar atoms: \t")[1].strip())
            elif pocket.startswith("\tAlpha sphere density"):
                Alpha_sphere_density.append(pocket.split("Alpha sphere density : \t")[1].strip())
            elif pocket.startswith("\tCent. of mass - Alpha Sphere max dist"):
                Cent_of_mass_Alpha_Sphere_max_dist.append(pocket.split("Cent. of mass - Alpha Sphere max dist: \t")[1].strip())
            elif pocket.startswith("\tFlexibility"):
                Flexibility.append(pocket.split("Flexibility : \t")[1].strip())

        df = pd.DataFrame()
        df["Pocket"] = pockets
        df["Score"] = Score
        df["Druggability_Score"] = Druggability_Score
        df["Number_of_Alpha_Spheres"] = Number_of_Alpha_Spheres
        df["Total_SASA"] = Total_SASA
        df["Polar_SASA"] = Polar_SASA
        df["Apolar_SASA"] = Apolar_SASA
        df["Volume"] = Volume
        df["Mean_local_hydrophobic_density"] = Mean_local_hydrophobic_density
        df["Mean_alpha_sphere_radius"] = Mean_alpha_sphere_radius
        df["Mean_alp._sph._solvent_access"] = Mean_alp_sph_solvent_access
        df["Apolar_alpha_sphere_proportion"] = Apolar_alpha_sphere_proportion
        df["Hydrophobicity_score"] = Hydrophobicity_score
        df["Volume_score"] = Volume_score
        df["Polarity_score"] = Polarity_score
        df["Charge_score"] = Charge_score
        df["Proportion_of_polar_atoms"] = Proportion_of_polar_atoms
        df["Alpha_sphere_density"] = Alpha_sphere_density
        df["Cent._of_mass_Alpha_Sphere_max_dist"] = Cent_of_mass_Alpha_Sphere_max_dist
        df["Flexibility"] = Flexibility
        df.to_csv(filename.split("_")[0] + "_stat.csv", index = False)
  
