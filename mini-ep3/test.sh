#!/bin/bash

max=${2:-3}

for i in `seq 1 $max`
do
    python3 $1 < "in"$i | diff "out"$i - > /dev/null

    ret_val=$?
    
    if [ "$ret_val" -eq 0 ]
    then
        echo "O teste [$i] passou com sucesso! :)"
    else
        echo "O teste [$i] falhou! :((("
    fi
done
