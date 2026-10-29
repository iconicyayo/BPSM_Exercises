#!/usr/bin/env python3

dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT" 

site = dna.find("GAATC")

if site != =1:
	cut = site + 1
	first = dna[:cut]
	second = dna["cut:]
	print (len(first), len(second))
else:
	print ("EcoRI site not found")
