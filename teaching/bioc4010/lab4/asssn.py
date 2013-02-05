# Open the file
filein = open("duckpolyprot.fasta")

# Skip line
filein.readline()

# Read in data
protein = filein.read()

# Remove end of lines
protein = protein.replace("\n","")

# Open outfile
fout = open("regions.fasta", "w")

# Region 1
fout.write(">rhv_like\n")
fout.write(protein[79:254]+"\n")

# Region 2
fout.write(">rhv_like\n")
fout.write(protein[336:485]+"\n")

# Region 3
fout.write(">Ras_like_GTPase\n")
fout.write(protein[754:909]+"\n")

# Region 4
fout.write(">P-loop NTPase\n")
fout.write(protein[1297:1397]+"\n")

# Region 5
fout.write(">RNA_dep_RNAP\n")
fout.write(protein[1236:2193]+"\n")

# Region 6
fout.write(">Peptidase_C3\n")
fout.write(protein[1632:7184]+"\n")

# Close the file
fout.close()
filein.close()
