import os, sys

#This function will seperate the overlapping and unique reads on the same chromosome, each in group.
#The output of this function will be two strings: one is the unique reads and the other is the overlapping reads

def overlap(infile):
    def remove_first_line(s):
        return s[s.find('\n')+1:s.rfind('\n')]
    overlapping = ""
    unique = ""
    prev_chromo = ""
    prev_start = 0
    prev_end = 0

    #reading the input file
    with open(infile, 'r') as to_check:
          lines=to_check.readlines()

    #iterating the bed file, line by line
    for line in lines:
        split_line = line[:-1].split("\t")
        chromo = str(split_line[0])
        start = int(split_line[1])
        end = int(split_line[2])

        #verifying whether the two successive reads are on the same chromosome, if not, the comparison will be skipped
        if chromo != prev_chromo:
            prev_chromo = chromo
            unique_reads = "%s\t%i\t%i\n" % (prev_chromo, prev_start, prev_end)
            unique += unique_reads
            prev_end = end
            prev_start = start
        else:
            #seperating the unique reads
            if start >= prev_end:
                unique_reads = "%s\t%i\t%i\n" % (prev_chromo, prev_start, prev_end)
                unique += unique_reads
                prev_end = end
                prev_start = start
            else:
                #seperating the overlapping reads
                overlapping_reads = "%s\t%i\t%i\n" % (prev_chromo, prev_start, prev_end)
                overlapping += overlapping_reads
                prev_end = end
                prev_start = start

    unique = remove_first_line(unique)
    unique_reads = "\n%s\t%i\t%i\n" % (chromo, start, end)
    unique += unique_reads
    return unique, overlapping
