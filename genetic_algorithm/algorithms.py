import numpy as np

class BasicGeneticAlgorithm:
    def __init__(self, first_individual, environment, fitness_func,
        population_size, n_generations, selection_depreciation=0.5):
        """Returns optimized solution based off initial individual and fitness
        function."""
        self.first_individual = first_individual
        self.environment = environment
        self.n_generations = n_generations
        self.population = self.initialize_population(
            first_individual, population_size)
        self.fitness_func = fitness_func
        self.population_size = population_size
        self.selection_depreciation = selection_depreciation

    def initialize_population(self, first_individual, size):
        """Initializes a population from the set of chromosomes from the first
        individual"""
        pool = first_individual
        return np.random.choice(pool, (size, len(pool)))

    def select(self):
        ranking = np.argsort([-self.fitness_func(individual, self.environment)
            for individual in self.population])
        new_population = [self.population[i] for i in ranking]
        weights = np.power(
            np.arange(self.population_size, 0, -1),
            self.selection_depreciation)
        probabilities = [weight/sum(weights) for weight in weights]
        selected = np.random.choice(
            np.arange(self.population_size),
            size=self.population_size,
            p=probabilities)
        self.population = [new_population[i] for i in selected]

    def crossover(self):
        pass

    def mutate(self):
        pass

    def run(self):
        for i in range(self.n_generations):
            self.select()
        return self.population
