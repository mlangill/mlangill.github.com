# Get Genome
fin = open('NC_003997.fna')
fin.readline()

genome = fin.read(50000)
genome = genome.replace('\n','')

fin.close()
print len(genome)