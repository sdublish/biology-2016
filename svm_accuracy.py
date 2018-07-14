"""Returns the SVM accuracy given data and weights"""

import sys
weight_file = sys.argv[1]
td = sys.argv[2]

input_1 = open(weight_file)
weights = []

for line in input_1:
    weights.append(float(line.strip()))

input_1.close()

constant = float(weights.pop())  # first number in weight file is always a constant
features = len(weights)  # remaining items in weights list corresponds to number of features
input_2 = open(td)

total = 0
real = 0

for line in input_2:
    data = line.strip().split()
    data_sum = constant  # beginning sum is always equal to constant
    total += 1

    for i in range(features):
        data_sum += weights[i] * float(data[i])

    # if the sum is greater than zero, data point should be classified as group 1
    # otherwise classified as group two
    # if conditions are met, then we were able to predict it properly
    if (data_sum > 0 and int(data[-1]) == 1) or (data_sum < 0 and int(data[-1]) == 2):
        real += 1

input_2.close()

percent = float(real)/float(total)
print("accuracy: {}".format(percent))
