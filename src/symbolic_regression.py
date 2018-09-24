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

def fill_population(population, desiredPopulationSize, fit, numberOfVariables):
    pop = population.copy()
    popSize = len(pop)

    for _ in range(desiredPopulationSize - popSize):
        pop.append(individual.Individual(fit, numberOfVariables))

    return pop

try:
    populationSize = int(sys.argv[1])
    generations = int(sys.argv[2])
    mutationProb = float(sys.argv[3])
    crossoverProb = float(sys.argv[4])
    kTournament = int(sys.argv[5])
    dataHolder = data.Data(sys.argv[6], sys.argv[7])
except:
    print('You are missing one or more parameters. Execute make help to print the help menu.')
    sys.exit(1)

fit = fitness.Fitness(dataHolder.train, dataHolder.test)
tour = selection.Tournament(kTournament)

for generation in range(generations):
    print('\n***Generation:', generation+1, '***')
    stats = statistics.Statistics()
    # If it's the first generation, generate the initial population
    if generation == 0:
        population = []
        for index in range(0, populationSize):
            population.append(individual.Individual(fit, dataHolder.nVariables, randomSeed=index))

    else:
        mut = mutation.Mutation(mutationProb, dataHolder.nVariables, generation)
        population = mut.mutate_population(population, fit)

        cross = crossover.Crossover(crossoverProb, dataHolder.nVariables, generation)
        population = cross.cross_population(population, fit, stats)

        population = tour.execute(population)
        population = fill_population(population, populationSize, fit, dataHolder.nVariables)

    stats.get_train_statistics(population)

stats.get_test_statistics(population)
