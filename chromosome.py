import random
import numpy as np
from settings import TOTAL_ITENS_BENEFIT, MAX_ITENS


itens = [[random.randint(1, MAX_ITENS), random.randint(1, TOTAL_ITENS_BENEFIT)] for i in range(MAX_ITENS)]


class Chromosome():

    def __init__(self, gene):
        self.gene = gene

    @property
    def fitness(self):
        total_size = 0
        total_benefit = 0

        for i in range(len(self.gene)):
            if self.gene[i]:
                total_size += itens[i][0]
                total_benefit += itens[i][1]

        return np.array([total_size, total_benefit])

    def __repr__(self):
        return "Chromosome: {} --- Fitness: {}".format(
            self.gene,
            self.fitness
        )
