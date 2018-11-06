import random
from settings import (
    BAG_SIZE,
    MAX_ITENS,
    POPULATION_SIZE,
    SELECTION_PERCENT,
    MUTATION_PERCENT,
    MAX_ITERATION,
    ITENS
)
from chromosome import Chromosome
from utils import (
    roulette_selection,
    crossover,
    chromosome_is_valid,
    mutate,
    best,
    get_bests
)

population = []
generation = 1
best_solution = None

print("Generating a initial valid population...")

while len(population) <= POPULATION_SIZE:
    gene = [random.randint(0, 1) for i in range(MAX_ITENS)]
    c = Chromosome(gene)

    population.append(c)

print("Searching the solution...")

while (generation < MAX_ITERATION):
    selected_population = []
    new_population = []
    elitism_selecteds_size = POPULATION_SIZE - int((POPULATION_SIZE * SELECTION_PERCENT) / 100)
    new_population.extend(
        get_bests(population, elitism_selecteds_size)
    )

    for i in range(int((POPULATION_SIZE * SELECTION_PERCENT) / 100)):
        selected_population.append(roulette_selection(population))

    selected_population = zip(
        selected_population,
        selected_population[int(len(selected_population) / 2):]
    )


    for x, y in selected_population:
        new_population.extend(crossover(x.gene, y.gene))

    population_to_mutate = int((POPULATION_SIZE * MUTATION_PERCENT) / 100)

    for i in range(population_to_mutate):
        new_population[random.randint(0, POPULATION_SIZE - 1)] = mutate(new_population[random.randint(0, POPULATION_SIZE - 1)].gene)

    population = new_population

    best_solution = best(population).fitness

    generation += 1

print(best(population).gene)
