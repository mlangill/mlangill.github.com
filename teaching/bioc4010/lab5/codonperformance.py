reffile = open('NC_003997.txt')

refstart = []
refstop = []

reffile.readline()

for i in  reffile:
    line = i.split()
    refstart.append(line[1])
    refstop.append(line[2])
reffile.close()

tesfile = open('prediction.txt')

tesstart = []
tesstop = []

tesfile.readline()

for i in  tesfile:
    line = i.split()
    tesstart.append(line[1])
    tesstop.append(line[2])
tesfile.close()

print "Start"
start_TP = len(set(refstart).intersection(set(tesstart)))
start_FN = len(set(refstart).difference(set(tesstart)))
start_FP = len(set(tesstart).difference(set(refstart)))

sn = start_TP / float(start_TP + start_FN)
sp = start_TP / float(start_TP + start_FP)
print "Sn = ", sn
print "Sp = ", sp
print "F-score= ", (2*sn * sp)/ (sn+sp)

print "\nStop"
start_TP = len(set(refstop).intersection(set(tesstop)))
start_FN = len(set(refstop).difference(set(tesstop)))
start_FP = len(set(tesstop).difference(set(refstop)))

sn = start_TP / float(start_TP + start_FN)
sp = start_TP / float(start_TP + start_FP)
print "Sn = ", sn
print "Sp = ", sp
print "F-score= ", (2*sn * sp)/ (sn+sp)
