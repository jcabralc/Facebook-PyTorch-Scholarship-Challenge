import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.

l =[5,6,7]


def softmax(l):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(l - np.max(l))
    return e_x / e_x.sum()

# The correct answer is
# [0.09003057317038046, 0.24472847105479764, 0.6652409557748219]
softmax(l)