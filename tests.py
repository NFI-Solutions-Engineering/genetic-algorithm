from genetic_algorithm import algorithms as algs
import unittest
import pandas as pd
import numpy as np
from os import path
from haversine import haversine, Unit
import random

root_dir = path.dirname(path.abspath(__name__))
instance_dir = path.join(root_dir, 'instance')

class BasicVRPGACase(unittest.TestCase):
    """Use case for solving VRP using a genetic algorithm"""
    filepath = path.join(instance_dir, 'demand.csv')
    demand_data = pd.read_csv(filepath) # rows for demand to route
    n = len(demand_data)
    initial_route_ids = np.random.randint(0, n-1, n) # each index maps to same position in demand
    n_generations = 10
    population_size = 10

    def setUp(self):
        self.algorithm = algs.BasicGeneticAlgorithm(
            first_individual=self.initial_route_ids,
            environment=self.demand_data,
            fitness_func=self.fitness_func,
            n_generations=self.n_generations,
            population_size=self.population_size)

    def tearDown(self):
        pass

    def fitness_func(self, individual, environment):
        """Return a fitness score for an individual. Lower scores rank
        higher."""

        def decode():
            """return individual represented with demand_data"""
            data = environment.copy()
            data['chromosomes'] = individual
            return data

        decoded = decode()

        # evaluate routes' total weight, total pallets, and total distance.
        max_weight = 45000
        max_pallets = 25
        max_distance = 50*2 # represent a total day of driving

        def calculate_distances(geocodes):
            return haversine((geocodes.prev_lat, geocodes.prev_lon),
                (geocodes.latitude, geocodes.longitude), unit=Unit.MILES)

        # tally penalties (dif from maxing out capacity + minimizing distance)
        weight_penalty = (
            max_weight - decoded.groupby('chromosomes')['Weight'].sum()
            ).abs().sum()

        pallet_penalty = (
            max_pallets - decoded.groupby('chromosomes')['Plts'].sum()
            ).abs().sum()

        distance_penalty = 0
        for chrom in decoded.chromosomes.unique():
            cols = ['latitude', 'longitude']
            stops = decoded.loc[decoded.chromosomes == chrom, cols].copy()
            stops['prev_lat'] = stops.latitude.shift()
            stops['prev_lon'] = stops.longitude.shift()
            distances = stops.apply(lambda x: calculate_distances(x), axis=1)
            distance_penalty += distances.sum()

        return weight_penalty + pallet_penalty + distance_penalty

    def test_algorithm(self):
        population = self.algorithm.run()
        i = random.randint(0, self.population_size)
        self.assertTrue(len(population[i]) == len(self.demand_data))

if __name__ == '__main__':
    unittest.main(verbosity=2)
