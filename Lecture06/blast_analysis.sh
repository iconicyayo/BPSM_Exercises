

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

## question 7: list the top 10 highest scoring hsps

## sort by bit score from highest to lowest and show the first 10
sort -k12,12nr blastdata.txt | head -10

### logic: look at coolumn 12, sort the HSPs by bit score (since higher = better), sort numerically rather than alphabetically, put the highest scors first and display only the first ten rows

## sort: sorts the lines, -k12, 12 uses columb 12 as the sort key, n sorts numerically, r reverses the sort order, head -10 displays the first ten lines

## question 8: list start positions where the subject accession contains aei

## read each line of the blast results
while read query subject identity length mismatches gaps qstart qend sstart send evalue bitscore
do
    ## check if the subject accession contains the letters aei
    if [[ "${subject}" == *AEI* ]]
    then
        ## show the subject and both start positions
        echo "${subject} query start: ${qstart} subject start: ${sstart}"
    fi
done < blastdata.txt

## Each subject sequence has an accession identifier, need to find HSPs whose subject accession contains AEI in the indicator. column 7 and column 9 are both potential start positions (where alignment begins in the query and in the subjecT), probs best to display both
## logic: read subject accession from column 2, check whether the text contains AEI, if it does display query and subject start positions, repeat this for every HSP 
## use *AEI* as the * means it will check for AEI anywhere in the accesion 

## question 9: count subject sequences with more than one hsp

## start the counter at zero
count=0

## count how many times each subject accession appears
while read number subject
do
    ## check if the subject has more than one hsp
    if test "${number}" -gt 1
    then
        ## increase the counter by one
        count=$((count+1))
    fi
done < <(cut -f2 blastdata.txt | sort | uniq -c)

## show how many different subjects have more than one hsp
echo "number of subjects with more than one hsp: ${count}"

## A single subject sequence can have multiple matching regions with the  query, producing multiple HSPs i.e. protein A and B have 3 and 2 HSPs and the answer would be 2 (as two proteins have >1 HSP) rather than 5 

## logic: extract all subject accessions (column 2), sort the accessions so identical ones are together, count how often each acession appears, and then count how many accession appears more than once

## count how many times each subject accession appears using cut -f2 blastdata.txt | sort | uniq -c
## uniq -c counts consecutive identical lines, so  sort must come before it
## the done << (cut.._) part of th script This is called process substitution lets the while loop read the results produced by the other commands while retaining the counter's value afterward.

## question 10: calculate the percentage of mismatches in each hsp

## read each line of the blast results
while read query subject identity length mismatches gaps qstart qend sstart send evalue bitscore
do
    ## check that the alignment length is greater than zero
    if test "${length}" -gt 0
    then
        ## calculate the percentage of mismatches
        percentage=$((mismatches * 100 / length))

        ## show the subject and its mismatch percentage
        echo "${subject} ${percentage}%"
    fi
done < blastdata.txt

## For every HSP, calculate what proportion of the alignment consists of mismatched amino acids.

##logic: read the alingment length from column 4, read number of mismatches from column 5, divide mismatches by alignment length, multiply that by 100 and display the percentage for each HSP 

## the script i wrote produces  an integer percentage, rounded down.

## question 11: put hsps into groups based on their bit scores

## read each line of the blast results
while read query subject identity length mismatches gaps qstart qend sstart send evalue bitscore
do
    ## remove the decimal part of the bit score for bash comparisons
    score=${bitscore%.*}

    ## check if the score is below 50
    if test "${score}" -lt 50
    then
        ## put the hsp into the low score group
        echo "${subject} low" >> low_scores.txt

    ## check if the score is below 200
    elif test "${score}" -lt 200
    then
        ## put the hsp into the medium score group
        echo "${subject} medium" >> medium_scores.txt

    ## put all remaining hsps into the high score group
    else
        echo "${subject} high" >> high_scores.txt
    fi
done < blastdata.txt

## count how many hsps are in each group
wc -l low_scores.txt medium_scores.txt high_scores.txt

## divide the HSPs into a small number of categories based on alignment quality
## use bit socre frmo column 12 (i.e. in question 7) and sort into low (below 50), medium (5-200), and high (above 200)
## ${bitscore%.*} removes the decimal part of a score such as 432.5, giving 432 so Bash can compare it as an integer.preserves the chosen group boundaries for non-negative scores.
