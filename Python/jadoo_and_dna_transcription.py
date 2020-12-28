'''dna_rna = str()
nucleotides = {'A', 'C', 'G', 'T', 'U'}
complement = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
b = set(input())
if b.issubset(nucleotides):
    for i in b:
        if i in complement:
            dna_rna = dna_rna+complement[i]
        else:
            dna_rna = dna_rna+i
    print(dna_rna)
else:
    print("Invalid Input")'''
a={'G':'C','C':'G','T':'A','A':'U'}
b=input()
try:print(''.join(a[i] for i in b))
except:print("Invalid Input")