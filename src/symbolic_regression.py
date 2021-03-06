#!/usr/bin/python3

import sys
import copy
import numpy as np
import libs.data as data
import libs.fitness as fitness
import libs.statistics as statistics
import libs.operators as operators
import libs.selection as selection
import libs.individual as individual
import libs.best_individual as best_individual

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
    activateElitistOperators = bool(int(sys.argv[10]))
except:
    print('You are missing one or more parameters. Execute make help to print the help menu.')
    sys.exit(1)

dataHolder = data.Data(trainCSVPath, testCSVPath)
fit = fitness.Fitness(dataHolder.train, dataHolder.test)
tour = selection.Tournament(kTournament)
bestInd = best_individual.BestIndividual()

if activateRandomSeed:
    np.random.seed(20182)

for generation in range(generations):
    print('\n***Generation:', generation+1, '***')
    stats = statistics.Statistics()
    
    # If it's the first generation, generate the initial population
    if generation == 0:
        population = []
        for index in range(0, populationSize):
            if index < populationSize/2:
                population.append(individual.Individual(fit, dataHolder.nVariables, method='grow'))
            else:
                population.append(individual.Individual(fit, dataHolder.nVariables, method='full'))

    stats.get_train_statistics(copy.deepcopy(population), dataHolder.train)

    bestInd.check_best_individual(min(population, key=lambda x: x.fitness))

    # Only do selection and operators if isn't the last generation
    if generation < generations - 1:
        newPopulation = []

        if activateElitism:
            newPopulation.append(selection.get_best_individual(population))

        newPopulation.extend(tour.execute(population))

        ops = operators.Operators(newPopulation, populationSize, mutationProb, crossoverProb, dataHolder.nVariables, fit, stats, activateElitistOperators)

        population = ops.execute()

# Gets the test statistics for the best individual amongst all generations
stats.get_test_statistics(bestInd.individual)
