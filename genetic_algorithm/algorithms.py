import numpy as np

class BasicGeneticAlgorithm:
    def __init__(self, individual, fitness_func, pop_size):
        """Returns optimized solution based off initial individual and fitness
        function."""
        self.population = self.initialize_population(individual, pop_size)
        self.fitness_func = fitness_func

    def initialize_population(self, first_individual, size):
        """Initializes a population from the set of chromosomes from the first
        individual"""
        pool = first_individual.chromosomes
        return np.random.choice(pool, (size, len(pool)))

    def select(self):
        pass

    def crossover(self):
        pass

    def mutate(self):
        pass

    def run(self):
        return self.population
