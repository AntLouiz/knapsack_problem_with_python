from cli import Cli

argparser = Cli.parse_args()

# Algorithm settings
POPULATION_SIZE = argparser.p
SELECTION_PERCENT = argparser.s
MUTATION_PERCENT = argparser.m
MAX_ITERATION = argparser.i


# Problem settings
BAG_SIZE = 165
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
MAX_ITENS = len(ITENS)
