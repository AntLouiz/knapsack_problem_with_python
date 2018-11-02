import random
from settings import (
    BAG_SIZE,
    MAX_ITENS,
    POPULATION_SIZE,
    SELECTION_PERCENT
)
from chromosome import Chromosome
from utils import roulette_selection, crossover

population = []


while len(population) != POPULATION_SIZE:
    gene = [random.randint(0, 1) for i in range(MAX_ITENS)]
    c = Chromosome(gene)
    if c.fitness[0] <= BAG_SIZE:
        # print("{} added".format(c))
        population.append(c)
    else:
        # print("{} denied".format(c))
        pass

print('Population collected.')


selected_population = []
new_population = []
random_selecteds_size = POPULATION_SIZE - int((POPULATION_SIZE * SELECTION_PERCENT) / 100)

for i in range(random_selecteds_size):
    selected_population.append(population[random.randint(0, len(population) - 1)])


for i in range(int((POPULATION_SIZE * SELECTION_PERCENT) / 100)):
    selected_population.append(roulette_selection(population))

selected_population = zip(
    selected_population,
    selected_population[int(len(selected_population) / 2):]
)


for x, y in selected_population:
    new_population.append(crossover(x.gene, y.gene))
    new_population.append(crossover(y.gene, x.gene))

print(new_population)
