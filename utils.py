import random
from chromosome import Chromosome
from settings import MAX_ITENS, BAG_SIZE, ITENS


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


def chromosome_is_valid(chromosome):
    if chromosome.fitness[0] <= BAG_SIZE:
        return True
    else:
        return False


def mutate(x):
    mutated_gene = []

    while True:
        random_gene_index = random.randint(0, MAX_ITENS - 1)
        for i in range(MAX_ITENS):
            if i == random_gene_index:
                mutated_gene.append(random.randint(0, 1))
            else:
                mutated_gene.append(x[i])

        mutated_chromosome = Chromosome(mutated_gene)

        if chromosome_is_valid(mutated_chromosome):
            break

        else:
            mutated_gene = []

    return mutated_chromosome
