
#!/usr/bin/env python3

# define a function to check the percentage of undetermined dna bases
# threshold=10 sets the default threshold to 10%
def base_counter(dna, threshold=10):

    # upper() converts the sequence to uppercase
    # this ensures lowercase bases are recognised correctly
    dna = dna.upper()

    # initialise a variable to count undetermined bases
    undetermined = 0

    # for loops through the dna sequence one base at a time
    for base in dna:

        # not in checks whether the base is absent from "ATGC"
        # any character other than a, t, g or c is counted
        if base not in "ATGC":

            # increase the undetermined base count by one
            undetermined = undetermined + 1

    # len() returns the total number of bases in the sequence
    # divide undetermined count by total length and multiply by 100
    percentage = (undetermined / len(dna)) * 100

    # display the percentage of undetermined bases
    print("undetermined bases:", percentage, "%")

    # > checks whether the percentage exceeds the threshold
    if percentage > threshold:

        # return True if the percentage exceeds the threshold
        return True

    # else runs when the percentage does not exceed the threshold
    else:
        return False


# test a sequence containing only determined bases
print("ATGCATGC:", base_counter("ATGCATGC"))

# test a sequence containing four undetermined bases
print("ATGCNNNN:", base_counter("ATGCNNNN"))

# test a sequence using a 20% threshold
print("ATGCATGN with 20% threshold:", base_counter("ATGCATGN", 20))

# test a sequence using a 30% threshold
print("ATGCNNNN with 30% threshold:", base_counter("ATGCNNNN", 30))

# verify the function outputs using assertions
assert base_counter("ATGCATGC") == False
assert base_counter("ATGCNNNN") == True
assert base_counter("ATGCATGN", 20) == False
assert base_counter("ATGCNNNN", 30) == True

# display confirmation if all assertions pass
print("all tests passed")

## results from the first four function calls:
## undetermined bases: 0.0 %
## ATGCATGC: False
## undetermined bases: 50.0 %
## ATGCNNNN: True
## undetermined bases: 12.5 %
## ATGCATGN with 20% threshold: False
## undetermined bases: 50.0 %
## ATGCNNNN with 30% threshold: True
##
## the assertions repeat the four undetermined-base percentage messages
## all tests passed

## logic: define a function with dna sequence and optional threshold; convert dna to uppercase; initialise an undetermined base counter; loop through each base using for; identify characters other than a, t, g or c using not in; increase the counter for each undetermined base; calculate percentage using len(); compare percentage against threshold using if and else; return true or false; display results using print(); verify outputs using assertions
