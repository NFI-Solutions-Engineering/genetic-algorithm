import pandas as pd
import numpy as np
__version__ = 'v0.1'

class Individual:
    pass

class Population(Individual):
    pass

class Environment:
    pass

class GeneticAlgorithm(Environment):
    def __init__(self, population, fitness):
        """returns optimized solution based off population and fitness
        function."""
        self.pop = population
        self.fit = fitness
