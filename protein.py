# protein synthesis simulation
import time, re

# read file in
inf = file('strand.dna', 'r')
infread = inf.read().lower()

print ' -genereating base pairs\n'
time.sleep(1)

DNA0 = list(infread)
DNA1 = []

# match base pairs
for s in DNA0:
    if s == 'a':
        DNA1.append('t')
    if s == 't':
        DNA1.append('a')
    if s == 'c':
        DNA1.append('g')
    if s == 'g':
        DNA1.append('c')

print ".".join(DNA0)
print ".".join(DNA1)
time.sleep(1)
    
print '\n -starting transcription to form mRNA\n'
time.sleep(1)

mRNA0 = []

# match base pairs, replace t with u
for s in DNA1:
    if s == 'c':
        mRNA0.append('g')
    if s == 'g':
        mRNA0.append('c')
    if s == 'a':
        mRNA0.append('u')
    if s == 't':
        mRNA0.append('a')

print ".".join(DNA1)
print ".".join(mRNA0)

print '\n -starting translation to form tRNA\n'
time.sleep(1)

tRNA0 = []

# match base pairs
for s in mRNA0:
    if s == 'a':
        tRNA0.append('g')
    if s == 'g':
        tRNA0.append('a')
    if s == 'c':
        tRNA0.append('u')
    if s == 'u':
        tRNA0.append('c')

print ".".join(mRNA0)
print ".".join(tRNA0)
    
print '\n -generating codons\n'
time.sleep(1)

# split tRNA into codons
codonstr = "".join(tRNA0)
codon = re.findall('...', codonstr)
print "/".join(codon)

print '\n -matching codon names\n'
time.sleep(1)

aminoacid = []

# match codons with amino acids
for a in codon:
    if a in ['uuu', 'uuc']:
        aminoacid.append('(Phe/F) Phenylalanine')
        
    if a in ['uua', 'uug', 'cuu', 'cuc', 'cua', 'cug']:
        aminoacid.append('(Leu/L) Leucine')

    if a in ['auu', 'auc', 'aua']:
        aminoacid.append('(Ile/I) Isoleucine')

    if a in ['aug']:
         aminoacid.append('(Met/M) Methionine')

    if a in ['guu', 'guc', 'gua', 'gug']:
        aminoacid.append('(Val/V) Valine')

    if a in ['ucu', 'ucc', 'uca', 'ucg']:
        aminoacid.append('(Ser/S) Serine')

    if a in ['ccu', 'ccc', 'cca', 'ccg']:
        aminoacid.append('(Pro/P) Proline')

    if a in ['acu', 'acc', 'aca', 'acg']:
        aminoacid.append('(Thr/T) Threonine')

    if a in ['gcu', 'gcc', 'gca', 'gcg']:
        aminoacid.append('(Ala/A) Alanine')

    if a in ['uau', 'uac']:
        aminoacid.append('(Tyr/Y) Tyrosine')

    if a in ['uaa']:
        aminoacid.append('Stop (Ochre)')

    if a in ['uag']:
        aminoacid.append('Stop (Amber)')

    if a in ['cau', 'cac']:
        aminoacid.append('(His/H) Histidine')

    if a in ['caa', 'cag']:
        aminoacid.append('(Gln/Q) Glutamine')

    if a in ['aau', 'aac']:
        aminoacid.append('(Asn/N) Asparagine')

    if a in ['aaa', 'aag']:
        aminoacid.append('(Lys/K) Lysine')

    if a in ['gau', 'gac']:
        aminoacid.append('(Asp/D) Aspartic acid')

    if a in ['gaa', 'gag']:
        aminoacid.append('(Glu/E) Glutamic acid')

    if a in ['ugu', 'ugc']:
        aminoacid.append('(Cys/C) Cysteine')

    if a in ['uga']:
        aminoacid.append('Stop (Opal)')

    if a in ['ugg']:
        aminoacid.append('(Trp/W) Tryptophan')

    if a in ['cgu', 'gc', 'cga', 'cgg']:
        aminoacid.append('(Arg/R) Arginine')

    if a in ['agu', 'agc']:
        aminoacid.append('(Ser/S) Serine')

    if a in ['aga', 'agg']:
        aminoacid.append('(Arg/R) Arginine')

    if a in ['ggu', 'ggc', 'gga', 'ggg']:
        aminoacid.append('(Gly/G) Glycine')
        
print " | ".join(aminoacid)
raw_input()
