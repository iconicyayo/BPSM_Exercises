
#!/usr/bin/env python3

# define a function to count frequently occurring kmers
# dna is the sequence, kmersize is the length of each kmer
# minfrequency is the frequency threshold
def count_kmers(dna, kmersize, minfrequency):

    # upper() converts the sequence to uppercase
    # this ensures lowercase and uppercase kmers are treated equally
    dna = dna.upper()

    # create an empty list to store extracted kmers
    kmers = []

    # range() generates the starting positions of the kmers
    # len() returns the total number of bases in the sequence
    # subtract kmersize and add one to include the final complete kmer
    for position in range(len(dna) - kmersize + 1):

        # slicing extracts a kmer beginning at the current position
        # position + kmersize determines the ending index
        kmer = dna[position:position + kmersize]

        # append() adds the extracted kmer to the list
        kmers.append(kmer)

    # create another empty list to store previously checked kmers
    checked = []

    # loop through all extracted kmers
    for kmer in kmers:

        # not in checks whether the current kmer has already been counted
        if kmer not in checked:

            # count() determines how many times the kmer occurs
            frequency = kmers.count(kmer)

            # > checks whether the frequency exceeds the threshold
            if frequency > minfrequency:

                # display the kmer and its frequency
                print("kmer:", kmer, "frequency:", frequency)

            # append() records the kmer as already checked
            # this prevents the same kmer being printed multiple times
            checked.append(kmer)


# store the example dna sequence
dna = "ATGCATCATG"

# display the input values before running the function
print("dna sequence:", dna)
print("kmer length:", 2)
print("minimum frequency:", 2)

# call the function using the example sequence
count_kmers(dna, 2, 2)

## results:
## dna sequence: ATGCATCATG
## kmer length: 2
## minimum frequency: 2
## kmer: AT frequency: 3

## logic: define a function with dna sequence, kmer length and minimum frequency; convert dna to uppercase; create a list to store kmers; use range() and len() to generate sliding window positions; extract kmers using slicing; append kmers to the list; create another list for previously checked kmers; loop through each kmer and use not in to avoid repeated counting; use count() to calculate frequencies; compare frequency against threshold using if and >; print qualifying kmers and their frequencies; call the function using the example dna sequence
