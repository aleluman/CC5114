from individual import *
from statistics import mean
import string

class Population:
    def __init__(self, pop_size, mutation_rate, fitness_function):
        self.population_size = pop_size
        self.mutation_rate = mutation_rate
        self.fitness_function = fitness_function
        self.population = []
        self.individual_fitness = []
        self.generation = 1

    def generate_individuals(self, gene_function, n_of_genes):
        self.population = [Individual(n_of_genes, self.mutation_rate, gene_function) for _ in
                           range(self.population_size)]
        self.calculate_fitness()

    def calculate_fitness(self):
        self.individual_fitness = [self.fitness_function(ind) for ind in self.population]

    def reproduce(self):
        self.population = [self.crossover(self.select_ind(), self.select_ind()) for _ in self.population]

    def select_ind(self):
        subgroup = min(self.population_size // 5, 5)
        choices = random.choices(self.individual_fitness, k=subgroup)
        return self.population[self.individual_fitness.index(max(choices))]

    def crossover(self, ind1, ind2):
        n = random.randint(0, len(ind1.genes))
        new_ind = Individual(len(ind1.genes), self.mutation_rate, ind1.generate_a_gene)
        new_ind.genes = ind1.genes[:n] + ind2.genes[n:]
        return new_ind

    def mutate_all(self):
        [ind.mutate() for ind in self.population]

    def evolve(self, print_info=True):
        while 1 not in self.individual_fitness:
            self.reproduce()
            self.mutate_all()
            self.calculate_fitness()
            if print_info:
                individual = self.population[self.individual_fitness.index(max(self.individual_fitness))].genes
                fitness = mean(self.individual_fitness)
                print(
                    "Generation {}, best individual: {}, average fitness: {}".format(self.generation, individual,
                                                                                     fitness))
            self.generation += 1

def f():
    return random.choice(string.ascii_lowercase)

    
def fit(x):
    n = 0
    for i in range(len(x.genes)):
        if palabra[i] == x.genes[i]:
            n += 1
    return n


if __name__ == "__main__":
    pop = Population(100, 0.01, fit)
    pop.generate_individuals(f, len(palabra))
    for i in range(100):
        pop.calculate_fitness()
        pop.reproduce()
        pop.mutate_all()
        print([x.genes for x in pop.population])
