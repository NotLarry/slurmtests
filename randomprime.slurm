#!/bin/bash
#SBATCH --mail-user=notlarry@hotmail.com
#SBATCH --mail-type=ALL
#SBATCH --ntasks=1
#SBATCH --time=00:00:10
#SBATCH --mem=100M
#SBATCH --output=python_job_slurm.out
#SBATCH --array=0-19

# These are comment lines

python3 /home/notlarry/slurmtest/randomprime.py
