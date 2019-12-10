#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 17:40:47 2019

Use: Gets the top 10 most repeated sequences
Required input: path to FASTA file
Output: Printed in TSV format

To run: python3 task2.py

@author: harini
"""
import re

seq_counts = dict()
path = "/home/harini/Desktop/sample_files-2/fasta/sample.fasta"

"""Using dictionary to get the sequnce occurences count"""
fh = open(path,"r")
for line in fh:
    if bool(re.search("^[ATGCN]+$",line)):
        line = line.strip()
        if line not in seq_counts:
            seq_counts[line] = 1
        else:
            seq_counts[line] += 1

"""Sorting the sequnces by highest count"""
sorted_seq_counts = sorted(seq_counts.items(), key=lambda x: x[1], reverse=True)
sorted_seq_counts = sorted_seq_counts[0:10]


"""Printing the sequences in TSV format"""
for seq in sorted_seq_counts:
    print("{0}\t{1}".format(seq[0],seq[1]))