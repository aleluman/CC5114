from population import *
import string
import numpy as np
import matplotlib.pyplot as plt

word = list('genetic')


def gene_f():
    return random.choice(string.ascii_lowercase + ' ')


def fitness_f(x):
    n = 0
    for i in range(len(x.genes)):
        if word[i] == x.genes[i]:
            n += 1
    return n / len(word)


if __name__ == "__main__":
    matrix = np.zeros([35, 23])
    i, j = 0, 0
    for pop_size in range(5, 40):
        for mutation_rate in np.arange(0.005, 0.05, 0.002):
            pop = Population(pop_size, mutation_rate, fitness_f)
            pop.generate_individuals(gene_f, len(word))
            pop.evolve(print_info=False)
            matrix[j][i] = pop.generation
            i += 1
            print(pop_size, mutation_rate)
        i = 0
        j += 1
    plt.matshow(matrix)
    plt.show()
