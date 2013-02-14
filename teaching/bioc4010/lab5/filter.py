myfile = open("NC_003997.GLIMMER3")
outfile = open("NC_003997.txt", "w")

outfile.write(myfile.readline())

for line in myfile:
    if "+" in line:
        outfile.write(line)

outfile.close()
myfile.close()