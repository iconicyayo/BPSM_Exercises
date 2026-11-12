
#!/usr/bin/env python3

# define a function to calculate the combined percentage of amino acids
# the default argument is a list of hydrophobic amino acid residues
# if no list is provided, python uses this default list
def amino_acid_percentage(protein, amino_acids=["A", "I", "L", "M", "F", "W", "Y", "V"]):

    # convert the protein sequence to uppercase to avoid case differences
    protein = protein.upper()

    # create a variable to store the total number of selected amino acids
    # start at zero because no residues have been counted yet
    total_count = 0

    # for loops through each amino acid in the supplied list
    # amino_acid stores the current residue during each iteration
    for amino_acid in amino_acids:

        # count() determines how many times the current amino acid occurs
        # upper() ensures the amino acid code matches the protein sequence
        count = protein.count(amino_acid.upper())

        # add the current count to the running total
        total_count = total_count + count

    # calculate the combined percentage of selected amino acids
    # len() returns the total number of residues in the protein
    percentage = (total_count / len(protein)) * 100

    # return the calculated percentage
    return percentage


# store the example protein sequence
protein = "MSRSLLLRFLLFLLLLPPLP"

# call the function with a list containing only methionine
# print() displays the returned percentage
print("methionine:", amino_acid_percentage(protein, ["M"]), "%")

# call the function with phenylalanine, serine and leucine
# the function adds together the counts of these three residues
print("F, S and L:", amino_acid_percentage(protein, ["F", "S", "L"]), "%")

# call the function without specifying an amino acid list
# python automatically uses the default hydrophobic residues
print("hydrophobic amino acids:", amino_acid_percentage(protein), "%")

# use assertions to check the function against expected results
assert round(amino_acid_percentage(protein, ["M"])) == 5
assert round(amino_acid_percentage(protein, ["F", "S", "L"])) == 70
assert round(amino_acid_percentage(protein)) == 65

# print confirmation if all assertions pass
print("all tests passed")

# logic: define a function with a protein sequence and optional amino acid list; use hydrophobic residues as the default; convert the protein to uppercase; initialise a running total at zero; loop through each amino acid using for; count occurrences using count(); add individual counts to the total; divide by sequence length and multiply by 100; return the percentage; use print() to display results for different lists; verify calculations using assertions

## results:
## methionine: 5.0 %
## F, S and L: 70.0 %
## hydrophobic amino acids: 65.0 %
## all tests passed
