myfile = open('duckprot.fasta')

protein = myfile.read()
protein = protein.replace('\n', '')

fout = open('out.fasta', 'w')

# First Sequence
fout.write( '>rhv1\n' )
fout.write( protein[121:252] + '\n')

fout.write( '>rhv2\n' )
fout.write( protein[361:481] + '\n')

fout.write( '>AIG1\n' )
fout.write( protein[754:909] + '\n')

fout.write( '>RNA_helicase\n' )
fout.write( protein[1327:1378] + '\n')

fout.write( '>Peptidase_C3\n' )
fout.write( protein[1627:1784] + '\n')

fout.write( '>RNA_dep_RNAP\n' )
fout.write( protein[1936:2193] + '\n')

fout.close()
