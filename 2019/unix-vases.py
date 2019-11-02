#!/usr/bin/env python
import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Vases
# 
# Australian Informatics Olympiad 2019
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of flowers.
N = None
a = None
b = None
c = None

# Open the input and output files.
input_file = open("vasesin.txt", "r")
output_file = open("vasesout.txt", "w")

# Read the value of N from the input file. 
N = int(input_file.readline().strip())

# TODO: This is where you should compute your solution. Store the number of
# flowers that should go in the first, second and third jars in the variables
# a, b and c. If it is impossible to arrange the flowers according to the
# rules, set each of these variables to 0.
if N < 6:
    a = 0
    b = 0
    c = 0
else:
    a = 1
    b = 2
    c = N - 3

# Write the answer to the output file.
output_file.write("%d %d %d\n" % (a, b, c))

# Finally, close the input/output files.
input_file.close()
output_file.close()
