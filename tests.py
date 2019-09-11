import genetic_algorithm as ga
import unittest


class GeneticAlgorithmCase(unittest.TestCase):
    def setUp(self):
        self.routes = ga.Individual() # example usage: VRP
        self.alg = ga.GeneticAlgorithm(self.routes, self.fitness_function)

    def fitness_function(self):
        pass

if __file__ == '__main__':
    unittest.main(verbosity=2)
