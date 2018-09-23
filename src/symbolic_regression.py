#!/usr/bin/python3

import sys
import libs.data as data
import libs.tree as tree
import libs.fitness as fitness
import libs.statistics as statistics
import libs.mutation as mutation
import libs.crossover as crossover
import libs.selection as selection
import libs.individual as individual

def fill_population(population, desired_population_size, fit, number_of_variables):
    pop = population.copy()
    pop_size = len(pop)

    for _ in range(desired_population_size - pop_size):
        pop.append(individual.Individual(fit, number_of_variables))

    return pop
    
population_size = int(sys.argv[1])
generations = int(sys.argv[2])
mutation_prob = float(sys.argv[3])
crossover_prob = float(sys.argv[4])
dataHolder = data.Data(sys.argv[5])

fit = fitness.Fitness(dataHolder.train)
tour = selection.Tournament(2)

for generation in range(generations):
    print('\n***Generation:', generation+1, '***')
    stats = statistics.Statistics()
    # If it's the first generation, generate the initial population
    if generation == 0:
        population = []
        for index in range(0, population_size):
            population.append(individual.Individual(fit, dataHolder.n_variables, random_seed=index))

    else:
        mut = mutation.Mutation(mutation_prob, dataHolder.n_variables, generation)
        population = mut.mutate_population(population, fit)

        cross = crossover.Crossover(crossover_prob, dataHolder.n_variables, generation)
        population = cross.cross_population(population, fit, stats)

        population = tour.execute(population)
        population = fill_population(population, population_size, fit, dataHolder.n_variables)

    stats.get_statistics(population)
