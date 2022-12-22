#!/bin/bash

#SBATCH --partition=ami100
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --gres=gpu

module load anaconda

module load cuda/11.4
anaconda activate causaldsr
python tmp.py
