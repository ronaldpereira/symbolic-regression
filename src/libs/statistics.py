#!/usr/bin/python3

def get_statistics(population):
    best_individual(population)
    worst_individual(population)
    mean_fitness(population)

def best_individual(population):
    best_ind = min(population, key=lambda x: x.fitness)
    print('Best Individual Fitness', best_ind.fitness)

def worst_individual(population):
    worst_ind = max(population, key=lambda x: x.fitness)
    print('Worst Individual Fitness', worst_ind.fitness)

def mean_fitness(population):
    total_fitness = 0
    for individual in population:
        total_fitness += individual.fitness
    print('Mean Fitness:', total_fitness / len(population))
