#!/bin/bash -l

#$ -pe smp 36
#$ -l mem=4G
#$ -l h_rt=6:0:0

#$ -cwd

export FWD_PORT=5100
export FWD_NODE=login12

umask 0077

module load xorg-utils matlab openssl/1.1.1u python/3.11.4

source matlab-demo/matlab-runtime/bin/activate
ssh -f -N -M -S $TMPDIR/ssh_control -R ${FWD_PORT}:localhost:${FWD_PORT} ${FWD_NODE}
jupyter lab --port=${FWD_PORT} > jupyter.${JOB_ID}.log 2>&1
ssh -S ${TMPDIR}/ssh_control -O stop ${FWD_NODE}
