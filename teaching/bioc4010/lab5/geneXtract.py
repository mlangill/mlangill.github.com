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
#fout = open('prediction.txt', 'w')

#Add the bogus header
#fout.write(">Just the usual bogus header\n")

# Set some variables
lastSTOP = 0
start = 0
stop = 0
while start != -1:
    # Find the first ATG after lastSTOP
    start = genome.find("ATG", lastSTOP)

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
        print "{0}\t{1}\t{2}".format(start+1,stop+1,stop-start)
        
        # We found a gene
        # Prepare the output line
        #frame = (start % 3) + 1
        #line = "ORF0000\t{0}\t{1}\t+{2}\t--\n".format(start+1,stop+1,frame)

        # Write the line to the outfile
        #fout.write(line)

        # Reset search to end of gene
        lastSTOP = stop
    else:
        # Reset search to just after last start codon.
        lastSTOP = start + 1

# Close outfile
#fout.close()
