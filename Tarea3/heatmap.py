from exercises import Population, fitness_65346_short, tree65346
import numpy as np
import matplotlib.pyplot as plt
"""displays a heat map to determine the optimal configuration of hyperparameters
to find the number 65346 with short trees.
WARNING: takes a lot of time to calculate"""

# population range from 50 to 1000 every 50 steps
# mutation range from 0 to 1 in 0.1 steps
pop_range = np.arange(50, 550, 50)
mut_range = np.arange(0, 1.1, 0.1)

if __name__ == "__main__":
    rating = []
    for i in pop_range:
        for j in mut_range:
            print("Computing... population size = {}, mutation rate = {}".format(i, j))
            pop = Population(i, j, fitness_65346_short, print)
            pop.generate_individuals(tree65346)
            y1, y2, y3 = pop.evolve(iterations=50, print_info=False, fitness_limit=1)
            rating.append(pop.generation)            
    rating = np.array(rating).reshape(pop_range.size, mut_range.size)
    plt.imshow(rating,extent=[mut_range.min(),mut_range.max(),pop_range.max(),pop_range.min()], aspect="auto", cmap="viridis_r")
    plt.ylabel("population size")
    plt.xlabel("mutation rate")
    plt.colorbar()
    plt.show()

