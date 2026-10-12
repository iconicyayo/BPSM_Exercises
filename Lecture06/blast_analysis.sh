

#!/bin/bash

## lecture06 blast analysis
## answer the questions using blastdata.txt


## question 1: list the subject accession for all hsps

## we know the subject accession is in column 2. Therefore, we only need to extract that column.
## show column 2 of the blast results
cut -f2 blastdata.txt

## cut extracts parts of each line, and -f2 means field (column) 2.

## question 2: list the alignment length and percent identity for all hsps

## show the alignment length and percent identity
cut -f3,4 blastdata.txt

## this displays identity first, then length, because cut retains the original column order

## ## read each hsp and give names to its 12 columns
while read query subject identity length mismatches gaps qstart qend sstart send evalue bitscore
do
    ## show the alignment length followed by percent identity
    echo "${length} ${identity}"
done < blastdata.txt

##  want length first so use while read function ; gives meaningful names to columns insteaed of remembering numbers

## question 3: show hsps with more than 20 mismatches

## read each line of the blast results
while read query subject identity length mismatches gaps qstart qend sstart send evalue bitscore
do
    ## check if the number of mismatches is greater than 20
    if test "${mismatches}" -gt 20
    then
        ## show the hsp that meets the condition
        echo "${query} ${subject} ${identity} ${length} ${mismatches} ${gaps} ${qstart} ${qend} ${sstart} ${send} ${evalue} ${bitscore}"
    fi
done < blastdata.txt

##logic: read an HSP, find its mismatch count (fifth column), check whether that count exceeeds 20, if it does display the HSP, repeat for every HSP
## -gt means great than 
## the if statement only runs the echo command if the statement is true

## question 4: show hsps shorter than 100 amino acids with more than 20 mismatches

## read each line of the blast results
while read query subject identity length mismatches gaps qstart qend sstart send evalue bitscore
do
    ## check if the length is below 100 and mismatches are above 20
    if test "${length}" -lt 100 && test "${mismatches}" -gt 20
    then
        ## show the hsp that meets both conditions
        echo "${query} ${subject} ${identity} ${length} ${mismatches} ${gaps} ${qstart} ${qend} ${sstart} ${send} ${evalue} ${bitscore}"
    fi
done < blastdata.txt

##  logic: can get the alignment length from column 4, number of mismatches from column 5, use a script to check if both conditions are true and only print HSP if both are satisfied 

## -lt means less than, -gt means greater than, && means AND(essential as OR would include HSPs meeting only one condition)


## question 5: list the first 20 hsps with fewer than 20 mismatches

## read each line and check the number of mismatches
while read query subject identity length mismatches gaps qstart qend sstart send evalue bitscore
do
    ## check if there are fewer than 20 mismatches
    if test "${mismatches}" -lt 20
    then
        ## show the hsp if it meets the condition
        echo "${query} ${subject} ${identity} ${length} ${mismatches} ${gaps} ${qstart} ${qend} ${sstart} ${send} ${evalue} ${bitscore}"
    fi
done < blastdata.txt | head -20

## logic: read an HSP, check whether mismatches are less than 20, if true display HSP, stop displaying after 20 HSPs that meet the condition are printed 

## head -20 after done because the first loop filters results, then head only displays first 20 filtered lines

## question 6: count how many hsps are shorter than 100 amino acids

## start the counter at zero
count=0

## read each line of the blast results
while read query subject identity length mismatches gaps qstart qend sstart send evalue bitscore
do
    ## check if the alignment length is below 100
    if test "${length}" -lt 100
    then
        ## increase the counter by one
        count=$((count+1))
    fi
done < blastdata.txt

## show the total number of hsps shorter than 100
echo "number of hsps shorter than 100 amino acids: ${count}"


## this time only need to count how many have an alignment length below 100 

## logic: start counter at zero, read alignment length for each HSP, if length than 100 increase counter by one, and once all HSP have been checked, display the counter

## count=$((count+1)) means take the current value of count, add 1, and save the new value.


