
#!/usr/bin/env python3

# define a function to count kmers above a specified frequency
# dna is the sequence, kmersize is the kmer length
# minfrequency is the number of occurrences that must be exceeded
def count_kmers(dna, kmersize, minfrequency):

    # upper() converts dna to uppercase
    # this prevents differences in letter case affecting results
    dna = dna.upper()

    # create an empty list to store extracted kmers
    kmers = []

    # range() generates the starting positions of each kmer
    # len() returns sequence length and kmersize determines window size
    # adding one ensures the final complete kmer is included
    for position in range(len(dna) - kmersize + 1):

        # slicing extracts the current kmer from the dna sequence
        kmer = dna[position:position + kmersize]

        # append() adds the extracted kmer to the list
        kmers.append(kmer)

    # create an empty list to track previously counted kmers
    checked = []

    # loop through each extracted kmer
    for kmer in kmers:

        # not in checks that the current kmer has not been counted already
        if kmer not in checked:

            # count() returns the total number of occurrences
            frequency = kmers.count(kmer)

            # > checks whether frequency exceeds the threshold
            if frequency > minfrequency:

                # display the kmer and its frequency
                print("kmer:", kmer, "frequency:", frequency)

            # append() marks the kmer as already checked
            checked.append(kmer)


# input() asks the user to enter a dna sequence
# the entered text is stored as a string
dna = input("enter dna sequence: ")

# input() asks for the kmer length
# int() converts the entered text into an integer
kmersize = int(input("enter kmer length: "))

# input() asks for the minimum frequency
# int() converts the entered value into an integer
minfrequency = int(input("enter minimum frequency: "))

# display the input values supplied by the user
print("dna sequence:", dna)
print("kmer length:", kmersize)
print("minimum frequency:", minfrequency)

# display a heading before the kmer results
print("kmers above the specified frequency:")

# call the function using the three user-supplied arguments
count_kmers(dna, kmersize, minfrequency)

## example results using ATGCATCATG, 2, 2:
## enter dna sequence: ATGCATCATG
## enter kmer length: 2
## enter minimum frequency: 2
## dna sequence: ATGCATCATG
## kmer length: 2
## minimum frequency: 2
## kmers above the specified frequency:
## kmer: AT frequency: 3
##
## actual results depend on the sequence and thresholds entered by the user

## logic: define a function with dna sequence, kmer length and minimum frequency arguments; convert dna to uppercase; create an empty list for kmers; use range() and len() to generate sliding window positions; extract kmers using slicing and append them to the list; create another list to track checked kmers; loop through kmers and count occurrences using count(); use if and > to identify kmers exceeding the threshold; display kmers and frequencies using print(); obtain user inputs using input(); convert numerical inputs using int(); call the function with the supplied values

