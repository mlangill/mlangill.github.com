
reffile = "NC_003997.txt"
testfile = 'prediction.XTG.txt'

def Xtract(fname):
    fin = open(fname)
    fin.readline()

    sta = []
    sto = []
    for line in fin:
        line = line.split()
        start = line[1]
        stop = line[2]
        sta.append(start)
        sto.append(stop)
        
    fin.close()
    return sta, sto

def NuclExtract(fname):
    fin = open(fname)
    fin.readline()

    nuc = []
    for line in fin:
        line = line.split()
        start = int(line[1])
        stop = int(line[2])
        nuc.extend(range(start,stop+1))
        
    fin.close()
    return nuc

def ExactExtract(fname):
    fin = open(fname)
    fin.readline()

    nuc = []
    for line in fin:
        line = line.split()
        nuc.append( line[1] + " " + line[2] )
        
    fin.close()
    return nuc
    
def Performance(real, pred):
    real = set(real)
    pred = set(pred)

    TP = len( real.intersection(pred) )
    FN = len( real.difference(pred) )
    FP = len( pred.difference(real) )

    Sn = float(TP) / (TP + FN)
    Sp = float(TP) / (TP + FP)
    Fs = (2*Sn*Sp) / (Sn + Sp)

    print "TP = ", TP
    print "FN = ", FN
    print "FP = ", FP
    print "Sn = ", Sn
    print "Sp = ", Sp
    print "Fs = ", Fs

# Get Reference data
realSTA, realSTO = Xtract(reffile)
realnuc = NuclExtract(reffile)
realEx = ExactExtract(reffile)
testSTA, testSTO = Xtract(testfile)
testnuc = NuclExtract(testfile)
testEx = ExactExtract(testfile)

print "START Codons statistics"
Performance(realSTA, testSTA)

print "-"*30

print "STOP Codons statistics"
Performance(realSTO, testSTO)

print "-"*30

print "\nNucleotide-level:"
Performance(realnuc, testnuc)

print "-"*30

print '\nExact Matching:'
Performance(realEx, testEx)