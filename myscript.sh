#!/bin/bash
echo "entering myscript"
for i in `seq 19`
do
    ./a.out -n ${i} -t 01:25:00 > ${i}.out &
done

./a.out -n 20 -t 01:25:00 > 20.out 
echo "exiting myscript"
