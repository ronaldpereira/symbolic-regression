#!/usr/bin/python3

import sys
import libs.data as data
import libs.tree as tree
import libs.fitness as fitness

treeMaxDepth = 7

class Individual:
    def __init__(self, randomSeed=None):
        self.root = self.generateRandomTree(randomSeed).root

    def generateRandomTree(self, randomSeed=None):
        return tree.RandomTree(dataHolder.numberOfVariables, randomSeed)

    def calculateFitness(self, fitness):
        self.fitness = fitness.calculate(self.root)


dataHolder = data.Data('./input/datasets/synth1/synth1-train.csv')

fit = fitness.Fitness(dataHolder.train)

population = []
for index in range(0, int(sys.argv[1])):
    population.append(Individual(index))
    population[index].calculateFitness(fit)

best_ind = min(population, key=lambda x: x.fitness)
print('Best Individual:')
print(best_ind.root.print_tree())
print('mininum fitness', best_ind.fitness)
