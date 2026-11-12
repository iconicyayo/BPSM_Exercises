

#!/usr/bin/env python3

# define a function to calculate the percentage of a particular amino acid
# def creates a reusable function with two input arguments
def amino_acid_percentage(protein, amino_acid):

    # upper() converts the protein sequence to uppercase
    # this ensures lowercase and uppercase letters are treated equally
    protein = protein.upper()

    # convert the specified amino acid to uppercase for the same reason
    amino_acid = amino_acid.upper()

    # count() counts how many times the amino acid occurs in the sequence
    count = protein.count(amino_acid)

    # len() returns the total number of amino acids in the protein
    # divide the count by total length and multiply by 100
    percentage = (count / len(protein)) * 100

    # return sends the calculated percentage back to the calling code
    return percentage


# store the example protein sequence in a variable
protein = "MSRSLLLRFLLFLLLLPPLP"

# print() displays the calculated percentages in the terminal
# calling the function with different residues gives different results
print("methionine:", amino_acid_percentage(protein, "M"), "%")
print("arginine:", amino_acid_percentage(protein, "R"), "%")
print("leucine:", amino_acid_percentage(protein, "L"), "%")
print("tyrosine:", amino_acid_percentage(protein, "Y"), "%")

# assert checks that the function returns the expected result
# round() rounds the percentage and == compares the two values
# an assertion error occurs if any test fails
assert round(amino_acid_percentage(protein, "M")) == 5
assert round(amino_acid_percentage(protein, "r")) == 10
assert round(amino_acid_percentage(protein, "L")) == 50
assert round(amino_acid_percentage(protein, "Y")) == 0

# display confirmation when all assertions pass
print("all tests passed")

# logic: define a function with protein and amino acid arguments; convert inputs to uppercase using upper(); count occurrences using count(); calculate percentage using len() and multiplication; return the result; use print() to display percentages for different amino acids; use assert and round() to check the expected results

## methionine: 5.0 %
## arginine: 10.0 %
## leucine: 50.0 %
## tyrosine: 0.0 %
## all tests passed
