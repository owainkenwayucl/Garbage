#!/bin/bash -l

#$ -pe smp 8
#$ -l mem=4G
#$ -l h_rt=6:0:0

#$ -cwd

export FWD_PORT=3270
export FWD_NODE=login12

umask 0077

module load python/3.9.10
source jupyterlab/bin/activate
ssh -f -N -M -S $TMPDIR/ssh_control -R ${FWD_PORT}:localhost:${FWD_PORT} ${FWD_NODE}
jupyter lab --port=${FWD_PORT} > jupyter.${JOB_ID}.log 2>&1
ssh -S ${TMPDIR}/ssh_control -O stop ${FWD_NODE}
