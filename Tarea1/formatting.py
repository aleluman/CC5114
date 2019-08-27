import numpy as np
from sklearn.model_selection import KFold


def normalize(array, nh=1, nl=0):
    dh = np.amax(array)
    dl = np.amin(array)
    return (array - dl) * ((nh - nl) / (dh - dl)) + nl


def denormalize(array, dh, dl, nh=1, nl=0):
    return ((dl - dh) * array - (nh * dl) + (dh * nl)) / (nl - nh)


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


def decode(array, encoding):
    decoded = []
    for i in array:
        decoded.append(encoding.keys()[encoding.values().index(i)])
    return decoded
