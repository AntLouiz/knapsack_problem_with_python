import random
from chromosome import Chromosome
from settings import MAX_ITENS, BAG_SIZE
from operator import attrgetter


def best(population):
    return max(population, key=attrgetter('fitness'))


def roulette_selection(population):
    population_fitness = [p.fitness for p in population]
    total_population_benefit = sum(population_fitness)
    random_number = random.randint(0, total_population_benefit)
    selected_position = 0

    while random_number > 0:
        selected_position += 1
        random_number -= population_fitness[selected_position - 1]

    return population[selected_position - 1]


def crossover(x, y):
    son1 = []
    son2 = []

    binary_mask = [random.randint(0, 1) for i in range(MAX_ITENS)]

    for i in range(len(binary_mask)):
        if binary_mask[i]:
            son1.append(x[i])
            son2.append(y[i])
        else:
            son1.append(y[i])
            son2.append(x[i])

    son1 = Chromosome(son1)
    son2 = Chromosome(son2)

    return [son1, son2]


def chromosome_is_valid(chromosome):
    if chromosome.total_size <= BAG_SIZE:
        return True
    else:
        return False


def mutate(x):
    mutated_gene = []

    random_gene_index = random.randint(0, MAX_ITENS - 1)

    for i in range(MAX_ITENS):
        if i == random_gene_index:
            mutated_gene.append(random.randint(0, 1))
        else:
            mutated_gene.append(x[i])

    mutated_chromosome = Chromosome(mutated_gene)

    return mutated_chromosome
