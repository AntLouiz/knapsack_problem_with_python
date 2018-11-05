import random

# Problem settings
BAG_SIZE = 165
MAX_ITENS = 10
TOTAL_ITENS_SIZE = 89
TOTAL_ITENS_BENEFIT = 92

# ITENS = [[random.randint(1, TOTAL_ITENS_SIZE), random.randint(1, TOTAL_ITENS_BENEFIT)] for i in range(MAX_ITENS)]

ITENS = [
    [23, 92],
    [31, 57],
    [29, 49],
    [44, 68],
    [53, 60],
    [38, 43],
    [63, 67],
    [85, 84],
    [89, 87],
    [82, 72]
]

"""
    Best solution to this parameters:
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
"""

# Algorithm settings
POPULATION_SIZE = 160
ELITISM_PERCENTUAL = 95
SELECTION_PERCENT = 95
MUTATION_PERCENT = 5
MAX_ITERATION = 50
