
#   Lab4 - ORF extract from a  genome
#   Christian Blouin
#   cblouin@cs.dal.ca
#   B00XXXXXX

# Open a file
myfile = open('duckhep.fasta')

# Skip a line
myline = myfile.readline()

# Read in the rest of the file
genome = myfile.read()

# Clean up the genome from newline characters
genome = genome.replace('\n', '')

# Output to user
print 'This genome contains', len(genome), 'characters.'

# Extract the orf
orf = genome[652:7408]

# Gene length
num_AA = len(orf) / 3.0
print "Gene length:", len(orf), "nucl. (", num_AA, " aa)"

# Write to FASTA
fileout = open('genome.fasta', 'w')

fileout.write('>Duck Polyprotein\n')

for lineindex in range(0, len(orf), 50):
    fileout.write( orf[lineindex : lineindex + 50] + "\n" )
    
fileout.close()    
