#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:39:55 2019

Use: Gets the annotation for coordinates
Required input: path to a GTF file
Output: Printed in TSV format

To run: python3 task3.py

@author: harini
"""

import pandas as pd

"""reading the file as a dataframe(vectorized)"""
gtf = pd.read_csv("/home/harini/Desktop/sample_files-2/gtf/hg19_annotations.gtf", sep = "\t", header = None)
gtf.columns = ["chr","source","type","start","end","score","strand","frame","annot","last"]
del gtf['last']

"""querying coordinates as dataframe"""
coordinates = {
        "chr": ["chr1","chrX","chr5","chr19","chr22"],
        "start": [6530945,134655166,139929652,5687293,22848382],
        "end": [6531050,134655244,139930497,5687387,22848500]}
query_df = pd.DataFrame(coordinates, columns = ["chr","start","end"])


"""finding the rows that match the query"""
for index, row in query_df.iterrows():
    output_df = gtf[(gtf["chr"] == query_df.chr[index]) & (gtf["start"] <= query_df.start[index])
    & (gtf["end"] >= query_df.end[index])]
    if output_df.empty:
        print("Coordinates not found")
    else:
        print(output_df)