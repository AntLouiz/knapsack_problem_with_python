import random


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
    return 1
