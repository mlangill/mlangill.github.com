'''
   ORF finder
   Christian Blouin
   B00XXXXXX
   cblouin@cs.dal.ca
'''

# Threshold
mingenelength = 100 * 3
maxgenomelen = 50000


# Get Genome
fin = open('NC_003997.fna')
fin.readline()

genome = fin.read()
genome = genome.replace('\n','')

fin.close()
print len(genome)

# useful variable
orfs = []

frame = 0
lastSTOP = 0
start = 0
fout = open('prediction.txt','w')
fout.write('>prediction\n')

while start != -1:
    #start = min (genome.find('ATG', lastSTOP), genome.find('TTG', lastSTOP))
    start = genome.find('ATG', lastSTOP)
    
    for i in range(start, len(genome), 3):
        codon = genome[i:i+3]
        if codon in ['TAA', 'TAG', 'TGA']:
            stop = i + 3
            break

    if stop - start >= mingenelength:
        print float(start)/len(genome)
        fout.write('ORF0000\t%d\t%d\t+%d\t--\n'%(start+1, stop, 1 + start%3))
        lastSTOP = stop
    else:
        lastSTOP = start + 1
        
fout.close()
    
