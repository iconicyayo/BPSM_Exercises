#!/usr/bin/env python3

# Read the genomic DNA sequence
with open("plain_genomic_seq.txt") as my_file:
    dna = my_file.read()

# Remove newlines and convert to uppercase
dna = dna.replace("\n", "").upper()
print("Total length:", len(dna))
print("Number of X:", dna.count("X"))

# Replace unknown or ambiguous bases with N
for base in dna:
    if base not in "ATCG":
        dna = dna.replace(base, "N")# Extract the first exon
exon1 = dna[0:63]
print("Unknown bases after cleaning:", dna.count("N"))

# Display the result
print(exon1)
print(len(exon1))

# Extract the second exon and intron
exon2 = dna[90:]
intron = dna[63:90]

# Combine the two coding regions
coding = exon1 + exon2

# Display the lengths
print("Exon 1:", len(exon1))
print("Intron:", len(intron))
print("Exon 2:", len(exon2))
print("Coding DNA:", len(coding))

# Write exon 1 to a FASTA file
with open("exon1.fasta", "w") as outfile:
    outfile.write(">exon1_length_" + str(len(exon1)) + "\n")
    outfile.write(exon1 + "\n")

# Write intron to a FASTA file
with open("intron.fasta", "w") as outfile:
    outfile.write(">intron_length_" + str(len(intron)) + "\n")
    outfile.write(intron + "\n")

# Write exon 2 to a FASTA file
with open("exon2.fasta", "w") as outfile:
    outfile.write(">exon2_length_" + str(len(exon2)) + "\n")
    outfile.write(exon2 + "\n")

# Write combined coding DNA
with open("coding.fasta", "w") as outfile:
    outfile.write(">coding_length_" + str(len(coding)) + "\n")
    outfile.write(coding + "\n")

# Write combined non-coding DNA
with open("noncoding.fasta", "w") as outfile:
    outfile.write(">noncoding_length_" + str(len(intron)) + "\n")
    outfile.write(intron + "\n")
