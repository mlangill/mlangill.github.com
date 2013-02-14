
def FindSTOP(genome, start, frame):
    for i in range(start, len(genome), 3):
        codon = genome[i:i+3]
        if codon in ['TAA', 'TAG', 'TGA']:
            return i + 3
    return False

mingenelength = 100 * 3


# Get Genome
fin = open('NC_003997.fna')
fin.readline()

genome = fin.read(50000)
genome = genome.replace('\n','')

fin.close()

# useful variable
orfs = []

frame = 0
lastSTOP = 0
start = 0

while start != -1:
    # Find either ATG or TTG
    start = min (genome.find('ATG', lastSTOP), genome.find('TTG', lastSTOP))
    
    # Find first in-frame STOP codons
    stop = FindSTOP(genome, start, frame)
    
    # Check for minimal length
    if stop - start >= mingenelength:
        # This ORF is assumed to be a gene
        print start + 1, stop, stop - start
        lastSTOP = stop
    else:
        lastSTOP = start + 1 
    
