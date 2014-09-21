#!/bin/bash

max=${2:-3}

for i in `seq 1 $max`
do
    for j in "a" "u"
    do
        python3 $1 "-"$j < "in"$i | diff "out"$i$j - > /dev/null

        ret_val=$?
        
        if [ "$ret_val" -eq 0 ]
        then
            echo "O teste [$i, $j] passou com sucesso! :)"
        else
            echo "O teste [$i, $j] falhou! :((("
        fi
    done
done
