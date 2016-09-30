
def to_rna(dna_seq):
    rna_seq= {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'U'}
    rna_conversion = ""
    for char in dna_seq.upper():
        if not rna_seq.has_key(char):
            return ""
        rna_conversion = rna_conversion + rna_seq[char]

    return rna_conversion
