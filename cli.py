import argparse

Cli = argparse.ArgumentParser()

Cli.add_argument('-p', type=int, action='store')
Cli.add_argument('-e', type=int, action='store')
Cli.add_argument('-s', type=int, action='store')
Cli.add_argument('-m', type=int, action='store')
Cli.add_argument('-i', type=int, action='store')
