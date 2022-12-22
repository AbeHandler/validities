#!/bin/bash 

#SBATCH --partition=ami100
#SBATCH --job-name=conda
#SBATCH --gres=gpu:1
#SBATCH --time=14:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1

# module load slurm/summit to access summit scheduler

source /curc/sw/anaconda3/latest

module load anaconda
conda activate causaldsr
python tmp.py
