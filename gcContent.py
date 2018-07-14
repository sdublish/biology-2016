"""Calculates the GC content given a string of nucleotides"""

from __future__ import division  # ensuring we have true division throughout the model

s = "tgcaagcatgcacatgtaccaggagaaaatgaagacaattgtggaaacttttagacttttcatcaactttctagtgtcacttttttgccgctttcctatctgatagttgcgaagactccgaagaaaatgagaatggtgaaggctagcatgctgatgcttc"

# alternatively, we could modify the program to take in an input file as one long string
# with something like this
# import sys
# s = open(sys.argv[1]).read

g_count = 0
c_count = 0

for base in s:
    if base == "g":
        g_count += 1

    elif base == "c":
        c_count += 1

gc_percent = (g_count + c_count)/len(s) * 100

print("The number of c nucleotides in the sequence are: {}".format(c_count))
print("The number of g nucleotides in sequence are: {}".format(g_count))
print("Total GC content in s is: {}".format(gc_percent))
