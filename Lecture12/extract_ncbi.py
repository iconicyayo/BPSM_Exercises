#!/usr/bin/env python3

# Read the NCBI FASTA file
with open("AJ223353.fasta") as my_file:
    dna = my_file.read()

# Remove the FASTA header
dna = dna.split("\n", 1)[1]

# Remove newlines and convert to uppercase
dna = dna.replace("\n", "").upper()

# Extract the coding sequence
coding = dna[28:409]

# Display sequence lengths
print("Total DNA:", len(dna))
print("Coding DNA:", len(coding))

# Extract the two non-coding regions
noncoding1 = dna[0:28]
noncoding2 = dna[409:808]

# Combine the non-coding regions
noncoding = noncoding1 + noncoding2

# Check the lengths
print("Non-coding 1:", len(noncoding1))
print("Non-coding 2:", len(noncoding2))
print("Total non-coding:", len(noncoding))

# Write the coding region
with open("AJ223353_coding.fasta", "w") as outfile:
    outfile.write(">AJ223353_coding_length_" + str(len(coding)) + "\n")
    outfile.write(coding + "\n")

# Write non-coding region 1
with open("AJ223353_noncoding1.fasta", "w") as outfile:
    outfile.write(">AJ223353_noncoding1_length_" + str(len(noncoding1)) + "\n")
    outfile.write(noncoding1 + "\n")

# Write non-coding region 2
with open("AJ223353_noncoding2.fasta", "w") as outfile:
    outfile.write(">AJ223353_noncoding2_length_" + str(len(noncoding2)) + "\n")
    outfile.write(noncoding2 + "\n")

# Write combined non-coding regions
with open("AJ223353_noncoding.fasta", "w") as outfile:
    outfile.write(">AJ223353_noncoding_length_" + str(len(noncoding)) + "\n")
    outfile.write(noncoding + "\n")
