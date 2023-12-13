#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=50
#SBATCH --time=03:00:00
#SBATCH --partition pbatch
date
sh myscript.sh
echo "ran my script"
date
