from utilities import *
from network import *
from activation_functions import *
import numpy as np


# methods to select the dataset for training
def train_seeds():
    data, x_len, y_len = load_data_wrapper("data/seeds_dataset.txt", range(0, 7), [7])
    net = Network([x_len, 12, y_len], rrelu, rrelu_d, 0.2)
    net.train(data, 2000)
    print("Confusion matrix for the seed dataset: ")
    net.confusion_matrix()
    net.plot_results()


def train_iris():
    data, x_len, y_len = load_data_wrapper("data/iris.data", range(0, 4), [4], delimiter=",", output_type="str")
    net = Network([x_len, 8, 5, y_len], sigmoid, sigmoid_d, 0.5)
    net.train(data, 2000)
    print("Confusion matrix for the iris dataset: ")
    net.confusion_matrix()
    net.plot_results()


if __name__ == "__main__":
    dataset = input("Select dataset (0: Seed dataset, Anything else: Iris dataset): ")
    if dataset == '0':
        train_seeds()
    else:
        train_iris()
