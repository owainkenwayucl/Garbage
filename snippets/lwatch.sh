#!/bin/bash

delay=${delay:-2}
scale=${scale:-2}
block=${block:-M}
x=`df -B${block} | grep lustre | awk '{print $3}'`

while [ true ]
do
sleep $delay
y=$x
x=`df -B${block} | grep lustre | awk '{print $3}'`
z=`echo "scale=$scale; ((${x%${block}}-${y%${block}})/$delay)" | bc`
echo `date +%s` use: $x delta: $z ${block}/s
done
