#!/usr/bin/python3

import sys
import libs.data as data
import libs.tree as tree
import libs.fitness as fitness
import libs.statistics as statistics

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

rand_node = population[5].root.get_random_node()
print(rand_node.print_tree())
rand_node = population[6].root.get_random_node()
print(rand_node.print_tree())
rand_node = population[8].root.get_random_node()
print(rand_node.print_tree())

statistics.get_statistics(population)
