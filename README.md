# protein.py

Tom Snelling, 10th January 2014

# about

protein.py is a python script that will build a string of amino acids from an initial strand of DNA.
I wrote it for a biology class, but thought I might as well share.

the process goes:
	create complementary dna strand from first one -> take a single strand and transcript to form 	mRNA (replace thymine with uracil) -> translate to form tRNA -> split tRNA into codons -> 	name codons, representing a protein

# usage

the strand.dna file is where the initial DNA sequence should be. formatting isn't too important as long as there aren't any spaces / random characters etc.

