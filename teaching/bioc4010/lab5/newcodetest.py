# Set some key constants 
minGeneLength = 100 * 3
readmaxlength = 50000

# Get Genome
fin = open('NC_003997.fna')
fin.readline()

genome = fin.read(readmaxlength)
genome = genome.replace('\n','')

fin.close()

# Open an outfile
fout = open('prediction.txt', 'w')

# Set some variables
lastSTOP = 0
start = 0
stop = 0

while start != -1:
    # Find the first ATG after lastSTOP
    start = genome.find("ATG", lastSTOP)
    # Find either ATG or TTG
    #start = min( genome.find("ATG", lastSTOP), genome.find("TTG", lastSTOP) )

    # Find the first in-frame STOP codon
    for i in range(start, len(genome), 3):
        # Define the codon
        codon = genome[i:i+3]
        # Check to see if it is a STOP codon
        if codon in ["TAA","TGA","TAG"]:
            stop = i + 2
            break

    # Is the ORF long enough?
    if stop - start >= minGeneLength:
        # We found a gene
        # Prepare the output line
        frame = (start % 3) + 1
        line = 'ORF0000\t'+ str(start+1) + '\t' + str(stop+1) + '\t+' + str(frame) + '\n'

        # Write the line to the outfile
        fout.write(line)

        # Print to the console (just because)
        print("starts=%d, ends=%d, length=%d"%(start+1, stop +1, stop - start))

        # Reset search to end of gene
        lastSTOP = stop
    else:
        # Reset search to just after last start codon.
        lastSTOP = start + 1

# Close outfile
fout.close()
