from genetic_algorithm import Population
import random
import string

ITERATIONS = 50
"""search for the binary string specified here"""
word = list('0010101011010001001011')


def gene_f():
    """a gene is represented with a 1 or 0"""
    return random.choice(['0', '1'])


def fitness_f(x):
    """the fitness function compares the position of each gene 
    with the optimal"""
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
    pop = Population(100, 0.01, fitness_f, print_func)
    pop.generate_individuals(gene_f, len(word))
    pop.evolve(iterations=ITERATIONS, fitness_limit=len(word))
