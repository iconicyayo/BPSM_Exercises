dna = ("ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCT"
"ACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCT"
"ATCATCGATCGATATCGATGCATCGACTACTAT")

exon1 = dna[:63]       # 63 bases!
intron = dna[63:90]    # 27 bases!
exon 2 = dna[90:]      # 33 bases!

coding = exon1 + exon2
print (coding)
print (len(coding) / len(dna) * 100)
print (exon1 + intron.lower() + exon2)

