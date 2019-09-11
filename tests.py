from genetic_algorithm import environment as env
from genetic_algorithm import algorithms as algs
import unittest
import pandas as pd
import numpy as np
from os import path

root_dir = path.dirname(path.abspath(__name__))
instance_dir = path.join(root_dir, 'instance')

class BasicVRPGACase(unittest.TestCase):
    """Use case for solving VRP using a genetic algorithm"""
    filepath = path.join(instance_dir, 'demand.csv')
    demand_data = pd.read_csv(filepath) # rows for demand to route
    initial_route_ids = demand_data.index.values # each index maps to same position in demand

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
