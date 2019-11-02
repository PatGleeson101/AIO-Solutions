#!/usr/bin/env python
import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for RPS
# 
# Australian Informatics Olympiad 2019
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of rounds contested.
N = None

# Ra, Pa and Sa are the number of times your opponent will throw rock, paper,
# and scissors, respectively.
Ra = None
Pa = None
Sa = None

# Rb, Pb and Sb are the number of times you will throw rock, paper, and
# scissors, respectively.
Rb = None
Pb = None
Sb = None

answer = None

# Open the input and output files.
input_file = open("rpsin.txt", "r")
output_file = open("rpsout.txt", "w")

# Read the value of N from the input file. 
N = int(input_file.readline().strip())

# Read the value of Ra, Pa and Sa from the input file. 
input_line = input_file.readline().strip()
Ra, Pa, Sa = map(int, input_line.split())

# Read the value of Rb, Pb and Sb from the input file. 
input_line = input_file.readline().strip()
Rb, Pb, Sb = map(int, input_line.split())

# TODO: This is where you should compute your solution. Store the answer (the
# maximum number of points you could score after N rounds have been played) in
# the variable answer.
w1 = min(Ra,Pb)
w2 = min(Pa,Sb)
w3 = min(Sa,Rb)

answer = w1 + w2 + w3
Ra -= w1
Pb -= w1
Pa -= w2
Sb -= w2
Sa -= w3
Rb -= w3

d1 = min(Ra,Rb)
d2 = min(Pa,Pb)
d3 = min(Sa,Sb)

Ra -= d1
Rb -= d1
Pa -= d2
Pb -= d2
Sa -= d3
Sb -= d3

answer -= Rb + Pb + Sb

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()
