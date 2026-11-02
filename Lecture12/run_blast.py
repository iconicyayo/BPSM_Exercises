#!/usr/bin/env python3

# Run BLASTX for the sequences generated in Mission One
import subprocess

files = [
    "exon1.fasta",
    "exon2.fasta",
    "intron.fasta",
    "coding.fasta",
    "noncoding.fasta",
    "AJ223353_coding.fasta",
    "AJ223353_noncoding1.fasta",
    "AJ223353_noncoding2.fasta",
    "AJ223353_noncoding.fasta"
]

# Run BLASTX against the nematode protein database
for filename in files:
    cmd = "blastx -query " + filename + " -db ../Lecture06/nem -out " + filename + ".blast.out -outfmt 6"
    subprocess.run(cmd, shell=True)

# Count reported alignments
for filename in files:
    results = subprocess.check_output(
        "wc -l " + filename + ".blast.out",
        shell=True
    ).decode("utf-8")
    print(results)

