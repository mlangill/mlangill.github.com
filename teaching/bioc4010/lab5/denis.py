# Dennis Orton, dn271654, dn271654@dal.ca

myfile = open("NC_003997.fna")
myfile.readline()
genome = fin.read()
genome = genome.replace("\n", "")
myfile.close

glimmer = open('prediction.txt', 'w')
header = '>Fasta Style'
glimmer.write(header)
glimmer.write("\n")

mingenomelength = 3 * 100
lastSTOP = 0
start = 0
stop = 0

while start != -1:
    start = genome.find("ATG", lastSTOP)

    for i in range(start, len(genome), 3):
        codon = genome[i:i+3]
        if codon in["TAA", "TGA", "TAG"]:
            stop = i + 2
            break
    if stop - start >= mingenelength:
        orfname = "ORF0000"
        frame = (start % 3) + 1

        line = orfname + "\t" + str(start) + "\t" + str(stop) + "\t" + str(frame) + "\t--\n" 
        glimmer.write(line)
        lastSTOP = stop + 1
    else:
        lastSTOP = lastSTOP + 1
glimmer.close()
