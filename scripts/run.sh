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

echo "$(date)" >  SUBMISSION
echo "Algorithm used for the submission: ${ALG}" >> SUBMISSION

echo "Zipping the solution..."
./scripts/zipper.sh

echo "The scores are:" >> SUBMISSION
total_score=0;
for f in $(find ./data/*.in  -printf "%f\n" | cut -d'.' -f1);
do
    partial_score=$(./scripts/scorer --in data/$f.in --solution out/$f.out)
    total_score=$(echo "$total_score + $partial_score" | bc)
    echo "- $f:  $partial_score" >> SUBMISSION;
done

echo "The total score of the submission is: ${total_score}" >&1 | tee -a SUBMISSION
echo "You can find a summary in the SUBMISSION file."