#!/usr/bin/env bash

ALG=$1

for input in data/*.in;
do
    output_filename="out/$(echo $input | cut -d'/' -f 2 | cut -d'.' -f 1).out"
    echo "Processing input $input, writing output in $output_filename"
    python3 -m hashcode19 --alg $ALG < $input > $output_filename
    if [[ $? -ne 0 ]]; then
        exit 1;
    fi

done

echo "$(date)" >>  SUBMISSION
echo "Algorithm used for the submission: ${alg)" >> SUBMISSION
