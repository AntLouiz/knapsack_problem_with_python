from settings import MAX_ITENS, ITENS, BAG_SIZE


class Chromosome():

    def __init__(self, gene):
        self.gene = gene
        self.total_benefit = 0
        self.total_size = 0

        for i in range(MAX_ITENS):
            if self.gene[i]:
                self.total_size += ITENS[i][0]
                self.total_benefit += ITENS[i][1]

    @property
    def fitness(self):
        if self.total_size > BAG_SIZE:
            return 0
        return self.total_size * self.total_benefit

    def __repr__(self):
        return "Fitness: {}".format(
            self.fitness
        )
