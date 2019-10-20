from knapsack import *
import numpy as np

"""displays a heat map to determine the optimal configuration of hyperparameters
on the knapsack problem. WARNING: takes a lot of time to calculate"""

# population range from 50 to 1000 every 50 steps
# mutation range from 0 to 1 in 0.1 steps
pop_range = np.arange(50, 1050, 50)
mut_range = np.arange(0, 1.1, 0.1)

if __name__ == "__main__":
    rating = []
    for i in pop_range:
        for j in mut_range:
            pop = Population(i, j, fitness_f, print_func)
            pop.generate_individuals(gene_f, 15)
            y1, y2, y3 = pop.evolve(iterations=ITERATIONS, print_info=False, fitness_limit=36)
            rating.append(y2[-1])
            print("Computing... population size = {}, mutation rate = {}".format(i, j))
    rating = np.array(rating).reshape(pop_range.size, mut_range.size)
    plt.imshow(rating,extent=[mut_range.min(),mut_range.max(),pop_range.min(),pop_range.max()], aspect="auto")
    plt.ylabel("population size")
    plt.xlabel("mutation rate")
    plt.colorbar()
    plt.show()

