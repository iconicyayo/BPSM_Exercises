
#!/bin/bash

## download the protein sequences if they are missing
if test ! -f nem.fasta
then
    wget https://live.bio.ed.ac.uk/bioinfmsc/nem.fasta
fi

## create the blast database
makeblastdb -in nem.fasta -dbtype prot -out nem
