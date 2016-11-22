#!/usr/bin/env python

import os
import argparse
from func import overlap

def unique_reads(args):
    l = 0
    #retrieving the two output groups (unique and overlapping reads)
    unique, overlapping = overlap(args.input)
    unover_file_name = "unique_reads_"+str(l)+".bed"
    unover_file_name = os.path.join(args.output, unover_file_name)
    #writing the unique reads to a seperate file
    with open(unover_file_name, 'w') as f1:
        f1.write(unique)
    #writing the overlapping reads to a seperate files
    with open("temp_overlapping_reads.bed", 'w') as f2:
        f2.write(overlapping)
    print unique

    #if there were any overlapping reads, the process will be repeated starting from the overlapping reads file
    #the process will be repeated until there is no more overlapping reads
    while os.stat("temp_overlapping_reads.bed").st_size > 0:
        l += 1
        args.input = "temp_overlapping_reads.bed"
        unique, overlapping = overlap(args.input)

        unover_file_name = "unique_reads_"+str(l)+".bed"
        unover_file_name = os.path.join(args.output, unover_file_name)
        with open(unover_file_name, 'w') as f1:
            f1.write(unique)
        with open("temp_overlapping_reads.bed", 'w') as f2:
            f2.write(overlapping)
        print unique
    os.remove("temp_overlapping_reads.bed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output', help="Path to the output files", default="output")
    args = parser.parse_args()
    unique_reads(args)
