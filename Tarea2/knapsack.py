from genetic_algorithm import Population
import random
import collections
import matplotlib.pyplot as plt

random.seed(1)
ITERATIONS = 100


def gene_f():
    return random.choice([(12, 4), (2, 2), (1, 2), (1, 1), (4, 10), (0, 0)])


def fitness_f(x):
    weight = 0
    value = 0
    for i in range(len(x.genes)):
        weight += x.genes[i][0]
        value += x.genes[i][1]
    if weight <= 15:
        return value
    return 0


def print_func(x):
    result = ""
    count = collections.Counter(x)
    for repetitions in count.keys():
        if count.get(repetitions) != 0 and repetitions[0] != 0:
            result += str(count.get(repetitions)) + \
                "x" + str(repetitions) + ", "
    return result


if __name__ == "__main__":
    pop = Population(1000, 0.1, fitness_f, print_func)
    pop.generate_individuals(gene_f, 15)
    y1, y2, y3 = pop.evolve(iterations=ITERATIONS)
    plt.plot(range(pop.generation - 1), y1)
    plt.plot(range(pop.generation - 1), y2)
    plt.plot(range(pop.generation - 1), y3)
    plt.legend(["minimum fitness", "average fitness", "maximum fitness"], loc=1)
    plt.ylabel("fitness")
    plt.xlabel("generation")
    plt.show()
