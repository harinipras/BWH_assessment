#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:03:50 2019

Use: Gets the propotion of nucleotide sequences of length > 30
Required input: path to a directory containing FASTQ files
Output: Printed in TSV format

To run: python3 task1.py
    
@author: harini
"""

import os
import sys
import re
        
def get_file_list(path1):
    """
    Use: gets the path for all fastq files in the directory
    Takes: filename(string)
    Returns: list of filepaths
    """
    file_names = list()
    for root, dirs, files in os.walk(path1, topdown=False):
       for name in files:
           check_file = os.path.join(root, name)
           if ".fastq" in check_file and "*" not in check_file:
               file_names.append(check_file)
    return(file_names)      

def get_fh(file,mode):
    """
    Use: Returns a filehandle for the file
    Takes: filename(string),mode(string)
    Returns: filehandle
    """
    try:
        fh = open(file,mode)
        return fh
    except ValueError as err:
        print("ValueError:",err)
        sys.exit(1)
    except IOError as err:
        print("IOError:",err)
        sys.exit(1)
    except TypeError as err:
        print("TypeError",err)
        sys.exit(1)
        
def get_propotion(fh):
    """
    Use: Gets the propotion of sequences with length > 30
    Takes: filehandle
    Returns: propotion(double)
    """
    seq_count = 0
    thirty_count = 0
    
    for line in fh:
        if bool(re.search("^@",line)):
            seq_count += 1
        elif not bool(re.search("^[ATGCN]+$",line)):
            if len(line) > 30: #Don't have to worry about appending sequences spanning multiple lines
                #Because we'll know if it's greater than 30 just by reading first line 
                thirty_count += 1
    if seq_count > 0:
        return(thirty_count/seq_count * 100)

def main():
    """Business Logic"""
    path1 = "/home/harini/Desktop/sample_files-2/fastq/"
    filenames = get_file_list(path1)
    for file in filenames:
        fh = get_fh(file,"r")
        prop = get_propotion(fh)
        path_array = file.split("/")
        print("{0}\t{1}%".format(path_array[len(path_array) - 1],prop))
main()