#!/bin/bash 

for i in `seq 20`
do
    ./a.out -n ${i} -t 00:10:00 > ${i}.out &
done

