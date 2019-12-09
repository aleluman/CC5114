from ast import AST
from arboles import *
from genetic_algorithm import Individual, Population
import matplotlib.pyplot as plt
import math
import random
import numpy as np

random.seed(16)
ITERATIONS = 1000


# gene function and fitness function to evaluate and evolve a finder of the number 10
tree10 = AST([AddNode, SubNode, MultNode], [2, 3, 5])
def fitness_10(ind):
    score = ind.genes.eval()
    return math.exp(-((score - 10) ** 2) / 100)


# gene function and fitness function to evaluate and evolve a finder of the number 65346
tree65346 = AST([AddNode, SubNode, MultNode, MaxNode], [25, 7, 8, 100, 4, 2])
def fitness_65346(ind):
    score = ind.genes.eval()
    return math.exp(-((score - 65346) ** 2) / 1000000)


# gene function and fitness function to evaluate and evolve a finder of the number 65346
# that limits the number of nodes on the tree and gives better score to trees with less nodes
def fitness_65346_short(ind):
    score = ind.genes.eval()
    score_fitness = math.exp(-((score - 65346) ** 2) / 1000000)
    tree_number_of_nodes = len(ind.genes.serialize())
    number_of_nodes_fitness = (50 - tree_number_of_nodes) / 50 if tree_number_of_nodes <= 50 else 0
    return (score_fitness * 9  + number_of_nodes_fitness) / 10  if score_fitness != 1 else 1


# gene function and fitness function to evaluate and evolve a finder of the number 65346
# with no repetition on the terminal nodes
tree_no_repetition = AST([AddNode, SubNode, MultNode], [25, 7, 8, 100, 4, 2])
def fitness_no_repetition(ind):
    score = ind.genes.eval()
    nodes = ind.genes.serialize()
    # making a list with only terminal nodes
    terminal_nodes = [x.eval() for x in nodes if isinstance(x, TerminalNode)]
    # checking if there are no repeated nodes
    if len(terminal_nodes) == len(set(terminal_nodes)):
        score_fitness = math.exp(-((score - 65346) ** 2) / 100000000)
        return score_fitness
    else: return 0


# gene function and fitness function to evaluate and evolve an equation finder of
# x² + x - 6
number_list = list(range(-10, 11))
number_list.extend(['x'] * 20)
tree_symbolic = AST([AddNode, SubNode, MultNode], number_list)
def fitness_symbolic(ind):
    def func(x):
        return x ** 2 + x - 6
    fitness_func = np.zeros(201)
    fitness_eval = np.zeros(201)
    # calculates the function directly and with the evaluation function of the tree
    for i in range(-100, 101):
        fitness_func[i + 100] = func(i)
        fitness_eval[i + 100] = ind.genes.eval({'x': i})
    # calculating the mean square error and converting it to an appropiate fitness function 
    fitness_error = ((fitness_func - fitness_eval) ** 2).mean()
    return 1 / (1 + fitness_error) 


# gene function and fitness function to evaluate and evolve an equation finder of
# (x + 3) / 3
tree_division = AST([AddNode, SubNode, MultNode, DivNode], number_list)
def fitness_division(ind):
    def func(x):
        return (x + 3) / 3
    fitness_func = np.zeros(201)
    fitness_eval = np.zeros(201)
    # catching divisions by zero
    try:
        for i in range(-100, 101):
            fitness_func[i + 100] = func(i)
            fitness_eval[i + 100] = ind.genes.eval({'x': i})
        fitness_error = ((fitness_func - fitness_eval) ** 2).mean()
        return 1 / (1 + fitness_error) 
    except ZeroDivisionError:
        return 0


# method to run each example
def run_exercise(fitness_func, gen_func, pop_size, mut_rate, title):
    pop = Population(pop_size, mut_rate, fitness_func, print)
    pop.generate_individuals(gen_func)
    y1, y2, y3 = pop.evolve(iterations=ITERATIONS, fitness_limit=1)
    plt.plot(range(pop.generation - 1), y1)
    plt.plot(range(pop.generation - 1), y2)
    plt.plot(range(pop.generation - 1), y3)
    plt.title(title)
    plt.legend(["minimum fitness", "average fitness", "maximum fitness"], loc=2)
    plt.ylabel("fitness")
    plt.xlabel("generation")
    plt.show()


if __name__ == "__main__":
    # To select which example to run
    option = input("Select example tu run:\n(1) Find number 10\n(2) Find number 65346\n(3) Find number 65346 (short trees version) \
        \n(4) Find number 65346 with no repetition in terminal nodes\n(5) Find equation x²+x-6\n(6) Find equation (x+3)/3\n")
    if option == '1':
        run_exercise(fitness_10, tree10, 10, 0.3, "Finding number 10")
    elif option == '2':
        run_exercise(fitness_65346, tree65346, 150, 0.3, "Finding number 65346")
    elif option == '3':
        run_exercise(fitness_65346_short, tree10, 150, 0.4, "Finding number 65346 (short trees)")
    elif option == '4':
        run_exercise(fitness_no_repetition, tree_no_repetition, 100, 0.5, "Finding number 65346 (no repetition)")
    elif option == '5':
        run_exercise(fitness_symbolic, tree_symbolic, 50, 0.1, "Finding x²+x-6")
    elif option == '6':
        run_exercise(fitness_division, tree_division, 50, 0.1, "Finding (x+3)/3")