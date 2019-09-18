import random


class Individual:
    def __init__(self, n_of_genes, mutation_rate, gene_function):
        self.number_of_genes = n_of_genes
        self.mutation_rate = mutation_rate
        self.generate_a_gene = gene_function
        self.genes = self.generate_genes()

    def generate_genes(self):
        return [random.choice(self.generate_a_gene()) for _ in range(self.number_of_genes)]

    def mutate(self):
        self.genes = [random.choice(self.generate_a_gene()) if random.random() <= self.mutation_rate
                      else gene for gene in self.genes]
