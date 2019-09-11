class BasicGeneticAlgorithm:
    def __init__(self, population, fitness):
        """returns optimized solution based off population and fitness
        function."""
        self.pop = population
        self.fit = fitness
