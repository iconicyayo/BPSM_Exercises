#!/usr/bin/env python3

# ==================================
# EXERCISE 1 - PROCESSING DNA
# ==================================

my_file = open('input.txt') ## open input.txt as my_file
output_file = open('cleaned.txt', 'w')

for eachline in my_file:
    dna = eachline.rstrip('\n') 
    cleaned_dna = dna[14:]
    print(len(cleaned_dna))
    output_file.write(cleaned_dna + '\n')

my_file.close()
output_file.close()

## for loop will go through each line indivudally in the file 
## dna = eachline.rstrip('\n') removes the blank line between each so we just work with the DNA bases
## cleaned_dna = dna[14:] produces a new variable contaiing the DNA squences with first fourteen based removed, starting at index 14. 
## print(cleaned_dna) prints the cleaned dna rather than 

# ==================================
# EXERCISE 2 - EXTRACTING EXONS
# ==================================

## Open the genomic DNA file containing the full DNA sequence
genomic_file = open('/localdisk/data/BPSM/Lecture13/genomic_dna2.txt')

## Read the DNA sequence into a variable and remove surrounding whitespace
genomic_dna = genomic_file.read().strip()

## Close the genomic DNA file because we have finished reading it
genomic_file.close()

## Open the file containing the start and stop positions of each exon
exon_file = open('/localdisk/data/BPSM/Lecture13/exons.txt')

## create empty string to store the combined exon sequences
combined_exons = ""

## Loop through the exon file, processing one line at a time
for eachline in exon_file:

    ## Remove whitespace and split the line at the comma to separate the positions
    positions = eachline.strip().split(',')

    ## Extract the first position from the list and convert it into an integer
    start = int(positions[0])

    ## Extract the second position from the list and convert it into an integer
    stop = int(positions[1])

    ## extract the exon sequence using the start and stop positions
    exon = genomic_dna[start:stop]

    ## add the extracted exon to the combined sequence
    combined_exons += exon
    ## Print the start and stop positions to check they have been read correctly
    print(start, stop)

## Close the exon file after the loop has finished
exon_file.close()

## open a new file to store the combined exon sequence
output_exons = open('combined_exons.txt', 'w')

## write the combined exon sequence to the file
output_exons.write(combined_exons + '\n')

## close the output file
output_exons.close()

## print the total length of the combined exon sequence
print(len(combined_exons))

## logic:
## read genomic dna file and store sequence as string;
## open exon file and use for loop to process each line;
## remove whitespace and split each line at comma into start/stop positions;
## access positions using list indices [0] and [1];
## convert positions from strings to integers using int();
## print positions to verify correct extraction;
## next, use positions to slice genomic dna and concatenate exons.

