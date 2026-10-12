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


