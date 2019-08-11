import unittest
import numpy as np


class Perceptron:
    def __init__(self, bias, weights):
        self.bias = bias
        self.weights = weights
        self.result = 0
        self.real_output = 0

    def output(self, inputs):
        assert self.weights.size == inputs.size, "Mismatch between inputs and weights size."

        self.result = np.sum(self.weights * inputs)
        if self.result + self.bias > 0:
            return 1
        else:
            return 0

    def learn(self, inputs, learning_rate, desired_output):
        diff = desired_output - self.output(inputs)
        self.weights = self.weights + (learning_rate * inputs * diff)
        self.bias += (learning_rate * diff)


class TestPerceptron(unittest.TestCase):
    def setUp(self):
        self.nand_perceptron = Perceptron(1.5, np.array([-1, -1]))
        self.and_perceptron = Perceptron(-1.5, np.array([1, 1]))
        self.or_perceptron = Perceptron(-0.5, np.array([1, 1]))

    def test_nand(self):
        self.assertEqual(self.nand_perceptron.output(np.array([1, 1])), 0)
        self.assertEqual(self.nand_perceptron.output(np.array([0, 1])), 1)
        self.assertEqual(self.nand_perceptron.output(np.array([1, 0])), 1)
        self.assertEqual(self.nand_perceptron.output(np.array([0, 0])), 1)

    def test_and(self):
        self.assertEqual(self.and_perceptron.output(np.array([1, 1])), 1)
        self.assertEqual(self.and_perceptron.output(np.array([0, 1])), 0)
        self.assertEqual(self.and_perceptron.output(np.array([1, 0])), 0)
        self.assertEqual(self.and_perceptron.output(np.array([0, 0])), 0)

    def test_or(self):
        self.assertEqual(self.or_perceptron.output(np.array([1, 1])), 1)
        self.assertEqual(self.or_perceptron.output(np.array([0, 1])), 1)
        self.assertEqual(self.or_perceptron.output(np.array([1, 0])), 1)
        self.assertEqual(self.or_perceptron.output(np.array([0, 0])), 0)


if __name__ == "__main__":
    unittest.main()
