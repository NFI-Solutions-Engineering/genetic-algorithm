from genetic_algorithm import environment as env
from genetic_algorithm import algorithms as algs
import unittest


class BasicGeneticAlgorithmCase(unittest.TestCase):
    def setUp(self):
        self.routes = env.Individual() # example usage: VRP
        self.alg = algs.BasicGeneticAlgorithm(
            self.routes, self.fitnes_func)

    def tearDown(self):
        pass

    def fitness_function(self):
        test = True
        return test

    def test_fitness(self):
        self.assertTrue(self.alg.fit())

if __name__ == '__main__':
    unittest.main(verbosity=2)
