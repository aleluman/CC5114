from genetic_algorithm import Population
import random
import string

ITERATIONS = 100
word = list('hello world')


def gene_f():
    return random.choice(string.ascii_lowercase + ' ')


def fitness_f(x):
    n = 0
    for i in range(len(x.genes)):
        if word[i] == x.genes[i]:
            n += 1
    return n 

def print_func(x):
    result = ""
    for gene in x:
        result += gene
    return result + ", "


if __name__ == "__main__":
    pop = Population(100, 0.05, fitness_f, print_func)
    pop.generate_individuals(gene_f, len(word))
    pop.evolve(iterations=ITERATIONS, fitness_limit=len(word))
