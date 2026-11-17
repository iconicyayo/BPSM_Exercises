
#!/usr/bin/env python3

# create a dictionary mapping dna codons to amino acids
# each key is a three-base codon
# each value is a one-letter amino acid code
# an underscore represents a stop codon

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
}


# define a function to translate a dna sequence
def translate(dna):

    # create an empty string to store the protein
    protein = ""

    # loop through the dna sequence in steps of three
    # stop before any incomplete final codon
    for i in range(0, len(dna) - 2, 3):

        # extract three bases using string slicing
        codon = dna[i:i+3]

        # retrieve the amino acid from the dictionary
        # return X if the codon is not recognised
        amino_acid = gencode.get(codon, "X")

        # add the amino acid to the protein string
        protein = protein + amino_acid

    # return the completed protein sequence
    return protein


# define a function to generate the reverse complement
def reverse_complement(dna):

    # create a dictionary of complementary dna bases
    complements = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
        "N": "N"
    }

    # create an empty string for the reverse complement
    reverse_dna = ""

    # reverse the dna sequence using string slicing
    reversed_sequence = dna[::-1]

    # loop through each base in the reversed sequence
    for base in reversed_sequence:

        # find the complementary base
        # use N if the base is not recognised
        complement = complements.get(base, "N")

        # add the complementary base to the new sequence
        reverse_dna = reverse_dna + complement

    # return the completed reverse complement
    return reverse_dna


# ask the user to enter a dna sequence
dna = input("Enter a DNA sequence: ")

# convert the sequence to uppercase and remove surrounding spaces
dna = dna.upper().strip()

# generate the reverse complement
reverse_dna = reverse_complement(dna)

# display the original and reverse complement sequences
print("\nOriginal DNA:", dna)
print("Reverse complement:", reverse_dna)


# translate all three forward reading frames
print("\nForward reading frames:")

# start at positions 0, 1 and 2
for frame in range(3):

    # remove the first 0, 1 or 2 bases
    sequence = dna[frame:]

    # translate the sequence using the function
    protein = translate(sequence)

    # display the frame number and translated protein
    print("Frame", frame + 1, ":", protein)


# translate all three reverse reading frames
print("\nReverse reading frames:")

# start at positions 0, 1 and 2 of the reverse complement
for frame in range(3):

    # remove the first 0, 1 or 2 bases
    sequence = reverse_dna[frame:]

    # translate the sequence using the function
    protein = translate(sequence)

    # display the frame number and translated protein
    print("Frame", frame + 1, ":", protein)


# logic summary
# read and standardise a dna sequence
# translate codons using a genetic code dictionary
# represent unknown codons with X
# generate the reverse complement using complementary bases
# translate three forward and three reverse reading frames
# print all six protein sequences
