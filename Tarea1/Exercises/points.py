import random
from perceptron import *
import numpy as np
import matplotlib.pyplot as plt


class Points:
    def __init__(self, n_points):
        self.n_points = n_points
        self.points = []
        self.outputs = np.zeros(n_points)
        self.a, self.b = self.generate_points()

    def generate_points(self):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        for i in range(self.n_points):
            p = [random.random() * 20 - 10, random.random() * 20 - 10]
            self.points.append(np.array(p))
            if p[1] > a * p[0] + b:
                self.outputs[i] = 1
        return a, b


def plot_points(n):
    points = Points(10000)
    perceptron = Perceptron(random.random(
    ) * 2 - 1, np.array([random.random() * 2 - 1, random.random() * 2 - 1]))
    for i in range(n):
        perceptron.learn(points.points[i], 0.1, points.outputs[i])
        if i % 50 == 0:
            print("Iteration: {}".format(i))
    real_outputs = [perceptron.output(x) for x in points.points]
    x_points = [x[0] for x in points.points]
    y_points = [x[1] for x in points.points]
    for i in range(1000):
        if real_outputs[i] <= 0.5:
            plt.scatter(x_points[i], y_points[i], c='r')
        else:
            plt.scatter(x_points[i], y_points[i], c='b')
    plt.plot(np.arange(-10, 10.1, 0.1),
             np.arange(-10, 10.1, 0.1) * points.a + points.b)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()


def plot_error(k):
    points = Points(k)
    errors = np.array([])
    perceptron = Perceptron(random.random(
    ) * 2 - 1, np.array([random.random() * 2 - 1, random.random() * 2 - 1]))
    for n in range(k):
        perceptron.learn(points.points[n], 0.05, points.outputs[n])
        real_outputs = np.array([perceptron.output(x)
                                 for x in points.points[:100]])
        errors = np.append(
            errors, 1 - np.abs(real_outputs - points.outputs[:100]).mean())
        if n % 50 == 0:
            print("Iteration: {}".format(n))
    plt.plot(range(k), errors)
    plt.ylim(0, 1)
    plt.show()


if __name__ == '__main__':
    plot_error(10000)
    plot_points(1000)
