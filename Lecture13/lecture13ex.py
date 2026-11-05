#!/usr/bin/env python3

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


