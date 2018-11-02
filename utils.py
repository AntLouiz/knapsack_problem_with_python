import random
from chromosome import Chromosome
from settings import MAX_ITENS, BAG_SIZE


def roulette_selection(population):
    population_fitness = [p.fitness[0] for p in population]
    total_population_benefit = sum(population_fitness)
    random_number = random.randint(0, total_population_benefit)
    selected_position = 0

    while random_number > 0:
        selected_position += 1
        random_number -= population_fitness[selected_position - 1]

    return population[selected_position - 1]


def crossover(x, y):
    son = []

    while len(son) == 0:
        binary_mask = [random.randint(0, 1) for i in range(MAX_ITENS)]

        for i in range(len(binary_mask)):
            if binary_mask[i]:
                son.append(x[i])
            else:
                son.append(y[i])

        son = Chromosome(son)

        if (son.fitness[0] > BAG_SIZE) or (son.fitness[0] == 0):
            son = []
        else:
            break

    return son
