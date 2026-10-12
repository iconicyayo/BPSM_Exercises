
#!/bin/bash

## run blastx using ncbi's remote protein database
blastx -query testsequence.fasta \
-db nr \
-remote \
-outfmt 7 > remote_blast.out
