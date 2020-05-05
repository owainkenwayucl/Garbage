#!/usr/bin/env bash
set -e
CMD=${CMD:-`which CovidSim_uk`}
ADMINDIR=${ADMINDIR:-data/admin_units}
PARAMDIR=${PARAMDIR:-data/param_files}
POPSDIR=${POPSDIR:-data/populations}
RUN=${RUN:-1}
THREADS=${THREADS:-1}
SEEDS=${SEEDS:-98798150 729101 17389101 4797132}
OUTPUT=${OUTPUT:-output}
R=${R:-3}
RS=`echo "8 k ${R} 2.0 / p" | dc`

rm -rf ${OUTPUT}-${RUN}
cp -R ${OUTPUT} ${OUTPUT}-${RUN}

$CMD /c:${THREADS} /A:${ADMINDIR}/United_Kingdom_admin.txt /PP:${PARAMDIR}/preUK_R0=2.0.txt /P:${PARAMDIR}/p_NoInt.txt /O:${OUTPUT}-${RUN}/UK_NoInt_R0=${R} /D:${OUTPUT}-${RUN}/UK_pop_density.bin /L:${OUTPUT}-${RUN}/Network_UK_T${THREAD}_R${R}.bin /R:${RS} ${SEEDS} | tee ${OUTPUT}-${RUN}/no_int.log
