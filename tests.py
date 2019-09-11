from genetic_algorithm import environment as env
from genetic_algorithm import algorithms as algs
import unittest
import pandas as pd
import numpy as np

class BasicVRPGACase(unittest.TestCase):
    """Use case for solving VRP using a genetic algorithm"""
    initial_route_ids = np.array([]) # each index maps to same position in demand
    demand_data = pd.DataFrame() # rows for demand to route
    def setUp(self):
        self.routes = env.Individual(self.initial_route_ids, self.demand_data)
        self.alg = algs.BasicGeneticAlgorithm(
            self.routes, self.fitness_func)

    def tearDown(self):
        pass

    def fitness_func(self):
        test = True
        return test

    def test_fitness(self):
        self.assertTrue(self.alg.fitness_func())

if __name__ == '__main__':
    unittest.main(verbosity=2)
