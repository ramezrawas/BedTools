datei = open(bed_file, "r")
lines = datei.readlines()
overlapped = lines(0)+"/n"
overlappedd == overlapped

for i in xrange(1, len(lines)):
    if col3(i) <= col2(i+1):
        overlapped = overlapped + lines(i) + "/n"

if overlapped != overlappedd
print overlapped > Overlapped_genes.bed
else:
    print "No overlapping genes"
