class Individual:
    def __init__(self, chromosomes, decoded):
        """Initialize an individual with a structure to represent
        its chromosomes and another to decode the chromosomes for
        evaluation"""
        self.chromosomes = chromosomes
        self.decoded = decoded
