"""Purpose: to compute the likelihood of a given set of observed nucleotide reads
 given the Phred score. Requires an input file with reads.
 Input file must be formatted so that each read is one line,
 with line format like 'nucleotide phred'. Results are printed onto console. """

import sys  # program run from the command line
from math import log10

nucleotide = []
score = []

# goes through input file and records the nucleotides and phred scores
# in two separate lists
# note equation for phred score: phred = -10 * log10(probability)
# ex: a phred score of 10 means that the probability that the base read is incorrect is 1 in 10


for line in open(sys.argv[1]):
    info = line.strip().split()
    nucleotide.append(info[0])
    score.append(float(info[1]))

file.close()


def log_probn(n1, n2, phred):
    """ Calculates the log 10 probability that the read is correct, based off phred score.
    Returns float number corresponding to log 10 probability.
    """
    if n1 == n2:  # if bases are the same
        ne = 1 - pow(10, (phred * -1 / 10))
        return log10(ne)

    else:  # if bases are different
        return (phred * -1 / 10)

# defining default log scores as zero
logA = 0
logG = 0
logT = 0
logC = 0

for i in range(len(score)):
    n = nucleotide[i]
    phred = score[i]
    # in log10 space so can just add probabilities together
    logA += log_probn('A', n, phred)
    logG += log_probn('G', n, phred)
    logT += log_probn('T', n, phred)
    logC += log_probn('C', n, phred)


# prints out results in form of nucleotide and then log10 probability
print("Nucleotide      Log10 Probability")
print("\nA                " + str(logA))
print("\nG                " + str(logG))
print("\nC                " + str(logC))
print("\nT                " + str(logT))
