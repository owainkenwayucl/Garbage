#!/bin/bash

set -e

arch=$(pwd)/opt/spack/linux-rhel7-skylake_avx512/gcc-9.2.0
c=${arch}/$(ls $arch | grep netcdf-c-  | head -n 1)
f=${arch}/$(ls $arch | grep netcdf-fortran- | head -n 1)

echo $c
echo $f

for a in $(ls ${c})
do
        for b in $(ls ${c}/${a})
        do
                ln -is ${c}/${a}/${b} ${f}/${a}/${b}
        done
done
