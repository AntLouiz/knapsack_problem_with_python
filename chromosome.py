import numpy as np
from settings import MAX_ITENS, ITENS


class Chromosome():

    def __init__(self, gene):
        self.gene = gene

    @property
    def fitness(self):
        total_size = 0
        total_benefit = 0

        for i in range(MAX_ITENS):
            if self.gene[i]:
                total_size += ITENS[i][0]
                total_benefit += ITENS[i][1]

        return np.array([total_size, total_benefit])

    def __repr__(self):
        return "Fitness: {}".format(
            self.fitness
        )
