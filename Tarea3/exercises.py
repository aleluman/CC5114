from ast import AST
from arboles import *
from genetic_algorithm import Individual, Population
import matplotlib.pyplot as plt
import math
import random

random.seed(13)
ITERATIONS = 1000


tree10 = AST([AddNode, SubNode, MultNode], [2, 3, 5])
def fitness_10(ind):
    score = ind.genes.eval()
    return math.exp(-((score - 10) ** 2) / 100)


tree65346 = AST([AddNode, SubNode, MultNode, MaxNode], [25, 7, 8, 100, 4, 2])
def fitness_65346(ind):
    score = ind.genes.eval()
    return math.exp(-((score - 65346) ** 2) / 1000000)


def fitness_65346_short(ind):
    score = ind.genes.eval()
    score_fitness = math.exp(-((score - 65346) ** 2) / 1000000)
    tree_number_of_nodes = len(ind.genes.serialize())
    number_of_nodes_fitness = (100 - tree_number_of_nodes) / 100 if tree_number_of_nodes <= 100 else 0
    return (score_fitness * 2 + number_of_nodes_fitness) / 3  if score_fitness != 1 else 1


tree_no_repetition = AST([AddNode, SubNode, MultNode], [25, 7, 8, 100, 4, 2])
def fitness_no_repetition(ind):
    score = ind.genes.eval()
    nodes = ind.genes.serialize()
    terminal_nodes = [x.eval() for x in nodes if isinstance(x, TerminalNode)]
    if len(terminal_nodes) == len(set(terminal_nodes)):
        score_fitness = math.exp(-((score - 65346) ** 2) / 100000000)
        return score_fitness
    else: return 0







if __name__ == "__main__":
    pop = Population(100, 0.5, fitness_no_repetition, print)
    pop.generate_individuals(tree_no_repetition)
    y1, y2, y3 = pop.evolve(iterations=ITERATIONS, fitness_limit=1)
    plt.plot(range(pop.generation - 1), y1)
    plt.plot(range(pop.generation - 1), y2)
    plt.plot(range(pop.generation - 1), y3)
    plt.legend(["minimum fitness", "average fitness", "maximum fitness"], loc=1)
    plt.ylabel("fitness")
    plt.xlabel("generation")
    plt.show()