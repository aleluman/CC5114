from statistics import mean
import random
### library to perform genetic operations on data


class Individual:
    """class to represent an individual and its genetic components"""
    def __init__(self, n_of_genes, mutation_rate, gene_function, print_func):
        """initializes an individual of the population with a specific number of genes, mutation rates,
        function to generate a gene and a print function to display information"""
        self.number_of_genes = n_of_genes
        self.mutation_rate = mutation_rate
        self.generate_a_gene = gene_function
        self.genes = self.generate_genes()
        self.print_func = print_func

    def generate_genes(self):
        """generate the specified number of genes for an individual"""
        return [self.generate_a_gene() for _ in range(self.number_of_genes)]

    def mutate(self):
        """checks for a chance to mutate each gene in an individual with the specified
        mutation rato"""
        self.genes = [self.generate_a_gene() if random.random() <= self.mutation_rate
                      else gene for gene in self.genes]

    def __str__(self):
        """prints to an appropiate format"""
        return self.print_func(self.genes)


class Population:
    """class to represent a population of individuals and genetic operations between them"""
    def __init__(self, pop_size, mutation_rate, fitness_function, print_func):
        """initializes a new population of individuals with the determined size and mutation rate, also includes
        a fitness function to evaluate each individual and a function for print formatting"""
        self.population_size = pop_size
        self.mutation_rate = mutation_rate
        self.fitness_function = fitness_function
        self.population = []
        self.individual_fitness = []
        self.generation = 1
        self.print_func = print_func

    def generate_individuals(self, gene_function, n_of_genes):
        """generate the number of individuals specified in the population size with a function to generate their genes
        and the number of genes they need"""
        self.population = [Individual(n_of_genes, self.mutation_rate, gene_function, self.print_func) for _ in
                           range(self.population_size)]
        self.calculate_fitness()

    def calculate_fitness(self):
        """calculate the fitness of each individual in the population with the specified fitness function"""
        self.individual_fitness = [
            self.fitness_function(ind) for ind in self.population]

    def reproduce(self):
        """selects two individuals and reproduces them for the next generation"""
        self.population = [self.crossover(
            self.select_ind(), self.select_ind()) for _ in self.population]

    def select_ind(self):
        """selects an individual of the population via the tournament method"""
        subgroup = min(self.population_size // 5, 5)
        choices = random.choices(self.individual_fitness, k=subgroup)
        return self.population[self.individual_fitness.index(max(choices))]

    def crossover(self, ind1, ind2):
        """selects randomly the index of a gene (n) and reproduces two individuals with the genetic information
        from the first from index 0 to n - 1 and genetic information of the second from n to the end"""
        n = random.randint(1, len(ind1.genes) - 1)
        new_ind = Individual(
            len(ind1.genes), self.mutation_rate, ind1.generate_a_gene, self.print_func)
        new_ind.genes = ind1.genes[:n] + ind2.genes[n:]
        return new_ind

    def mutate_all(self):
        """calls the mutate method for each individual of the population"""
        [ind.mutate() for ind in self.population]

    def evolve(self, print_info=True, iterations=200, fitness_limit=1000):
        """evolves the population by reproducing the best individuals based on the fitness function, mutates them 
        calculates their fitness. Returns three arrays with the minimum, average and maximum fitness on each 
        generation. The population can be evolved either until a maximum number of iterations is reached or until
        certain fitness is reached"""
        min_fitness = []
        avg_fitness = []
        max_fitness = []
        n = 0
        while n < iterations and max(self.individual_fitness) < fitness_limit:
            best = list(self.population[self.individual_fitness.index(
                max(self.individual_fitness))].genes)
            self.reproduce()
            self.mutate_all()
            self.population[0].genes = best
            self.calculate_fitness()
            min_fitness.append(min(self.individual_fitness))
            avg_fitness.append(mean(self.individual_fitness))
            max_fitness.append(max(self.individual_fitness))
            # prints info of the evolution process on console
            if print_info:
                individual = self.population[self.individual_fitness.index(
                    max(self.individual_fitness))]
                print(
                    "Generation {}, best individual: {}average fitness: {}".format(self.generation, individual,
                                                                                   avg_fitness[-1]))
            self.generation += 1
            n += 1
        return min_fitness, avg_fitness, max_fitness
