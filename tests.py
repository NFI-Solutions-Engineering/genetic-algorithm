from genetic_algorithm import environment as env
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
    population_size = 10

    def setUp(self):
        self.routes = env.Individual(self.initial_route_ids, self.demand_data)
        self.algorithm = algs.BasicGeneticAlgorithm(
            self.routes, self.fitness_func, pop_size=self.population_size)

    def tearDown(self):
        pass

    def fitness_func(self, individual):
        """Return a fitness score for an individual. Lower scores rank
        higher."""

        def decode():
            """return individual represented with demand_data"""
            data = self.decoded.copy()
            data['chromosomes'] = individual.chromosomes
            return data

        decoded = decode()

        # evaluate routes' total weight, total pallets, and total distance.
        max_weight = 45000
        max_pallets = 25
        max_distance = 50*2 # represent a total day of driving

        def calculate_distances(geocodes):
            return haversine(
                geocodes.prev_lat, geocodes.prev_lon, geocodes.latitude,
                geocodes.longitude, unit=Unit.MILES)

        # count the number of penalties
        weight_penalty = (
            decoded.groupby('chromosomes')['Weight'].sum() > max_weight).sum()
        pallet_penalty = (
            decoded.groupby('chromosomes')['Plts'].sum() > max_pallets).sum()
        distance_penalty = 0
        for chrom in decoded.chromosomes.unique():
            cols = ['latitude', 'longitude']
            stops = decoded.loc[decoded.chromosomes == chrom, cols].copy()
            stops['prev_lat'] = stops.latitude.shift()
            stops['prev_lon'] = stops.longitude.shift()
            distances = stops.apply(lambda x: calculate_distances(x), axis=1)
            distance_penalty += (distance > max_distance).sum()

        return weight_penalty + pallet_penalty + distance_penalty

    def test_algorithm(self):
        population = self.algorithm.run()
        i = random.randint(0, self.population_size)
        self.assertTrue(len(population[i]) == len(self.demand_data))

if __name__ == '__main__':
    unittest.main(verbosity=2)
