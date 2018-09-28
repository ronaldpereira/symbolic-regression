#!/usr/bin/python3

import sys
import libs.data as data
import libs.tree as tree
import libs.fitness as fitness
import libs.statistics as statistics
import libs.operands as operands
import libs.selection as selection
import libs.individual as individual

try:
    populationSize = int(sys.argv[1])
    generations = int(sys.argv[2])
    mutationProb = float(sys.argv[3])
    crossoverProb = float(sys.argv[4])
    kTournament = int(sys.argv[5])
    trainCSVPath = str(sys.argv[6])
    testCSVPath = str(sys.argv[7])
    activateRandomSeed = bool(int(sys.argv[8]))
    activateElitism = bool(int(sys.argv[9]))
except:
    print('You are missing one or more parameters. Execute make help to print the help menu.')
    sys.exit(1)

dataHolder = data.Data(trainCSVPath, testCSVPath)
fit = fitness.Fitness(dataHolder.train, dataHolder.test)
tour = selection.Tournament(kTournament)

for generation in range(generations):
    print('\n***Generation:', generation+1, '***')
    stats = statistics.Statistics()
    # If it's the first generation, generate the initial population
    if generation == 0:
        population = []
        for index in range(0, populationSize):
            population.append(individual.Individual(fit, dataHolder.nVariables, randomSeed=index if activateRandomSeed else None))

    else:
        newPopulation = []

        if activateElitism:
            newPopulation.append(selection.get_best_individual(population))

        newPopulation.extend(tour.execute(population))

        ops = operands.Operands(newPopulation, populationSize, mutationProb, crossoverProb, dataHolder.nVariables, fit, stats, randomSeed=index if activateRandomSeed else None)

        population = ops.execute()

    stats.get_train_statistics(population, dataHolder.train)

stats.get_test_statistics(population)
