from population import Population
import random
import string
import numpy as np
import matplotlib.pyplot as plt

word = list('hello world')


def gene_f():
    return random.choice(string.ascii_lowercase + ' ')


def fitness_f(x):
    n = 0
    for i in range(len(x.genes)):
        if word[i] == x.genes[i]:
            n += 1
    return n / len(word)


if __name__ == "__main__":
    pop = Population(100, 0.05, fitness_f)
    pop.generate_individuals(gene_f, len(word))
    pop.evolve()

