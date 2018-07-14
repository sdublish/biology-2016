"""Creates a random nucleotide sequence of As and Ts depending on the length provided"""

import sys
from random import random

length = int(sys.argv[1])
file_name = sys.argv[2]
input_file = open(file_name)
t_dict = {}
output = ''

for line in input_file:
    t = line.strip().split()
    key = (t[0], t[1])
    t_dict[key] = float(t[2])

input_file.close()

if length >= 1:
# this is an if statement in order to take into account
# the times people might enter 0 or a negative number for the length of the sequence
#(aka to make sure the code prints out something which makes sense)
    r = random()
    if r < .5:  # 50% chance to start with A
        output = 'A'
    else:  # 50% chance to start with T
        output = 'T'


while len(output) < length:
    r = random()  # random number which we will compare to probability
    last_n = output[-1]
    prob1 = t_dict[(last_n, 'A')]

    if r < prob1:  # if random number is less than probability
        output += 'A'

    else:
        output += 'T'


print(output)
