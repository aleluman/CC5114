import numpy as np


def normalize(array, nh=1, nl=0):
    return (array - array.min(0)) * ((nh - nl) / array.ptp(0)) + nl


def one_hot_encoding(array):
    labels = np.unique(array)
    number_of_labels = labels.size
    encoded = {}
    for i in range(number_of_labels):
        encoding = np.zeros(number_of_labels)
        encoding[i] = 1
        encoded[labels[i]] = encoding
    return encoded


def encode(array, encoding):
    encoded = []
    for i in array:
        encoded.append(encoding[i])
    return encoded
