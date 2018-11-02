import random
from settings import (
    BAG_SIZE,
    MAX_ITENS,
    POPULATION_SIZE,
    SELECTION_PERCENT,
    MUTATION_PERCENT,
    MAX_ITERATION
)
from chromosome import Chromosome
from utils import (
    roulette_selection,
    crossover,
    chromosome_is_valid,
    mutate
)

population = []
generation = 1

while len(population) != POPULATION_SIZE:
    gene = [random.randint(0, 1) for i in range(MAX_ITENS)]
    c = Chromosome(gene)

    if chromosome_is_valid(c):
        population.append(c)


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


population_to_mutate = int((POPULATION_SIZE * MUTATION_PERCENT) / 100)

for i in range(population_to_mutate):
    new_population[random.randint(0, MAX_ITENS - 1)] = mutate(new_population[random.randint(0, MAX_ITENS - 1)].gene)

print(new_population)
