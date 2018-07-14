""" Calculates the global alignment score given two sequences and a scoring matrix.
Sequences must be same length. Note the sequences must have already been aligned."""

import sys

sequence1 = sys.argv[1]
sequence2 = sys.argv[2]

matrix = sys.argv[3:]
# matrix order is [gap, different, same]

align_score = 0

for i in range(len(sequence1)):
    if sequence1[i] == sequence2[i]:  # nucleotides are the same
        align_score += float(matrix[2])

    elif sequence1[i] == "-" or sequence2[i] == "-":  # gap is found
        align_score += float(matrix[0])

    else:  # nucleotides are different
        align_score += float(matrix[1])

print("Score = {}".format(align_score))
