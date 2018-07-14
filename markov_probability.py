""" Calculates the Markov probability given a sequence and a transition matrix """

import sys
sequence = sys.argv[1]
file_name = sys.argv[2]

input_file = open(file_name)
transition = {}
probability = .25  # the probability of starting with any nucleotide is 25%

for line in input_file:
    line_info = line.split()
    key = (line_info[0], line_info[1])
    t_value = float(line_info[2])
    transition[key] = t_value

input_file.close()

for i in range(len(sequence) - 1):
    key = (sequence[i], sequence[i+1])
    probability *= transition[key]

print("Probability: {}".format(probability))
