#!/usr/bin/python3

import sys
import libs.data as data
import libs.tree as tree
import libs.fitness as fitness
import math

treeMaxDepth = 7

class Individual:
    def __init__(self, randomSeed=None):
        self.root = self.generateRandomTree(randomSeed).root

    def generateRandomTree(self, randomSeed=None):
        return tree.RandomTree(dataHolder.numberOfVariables, randomSeed)

dataHolder = data.Data('./input/datasets/synth1/synth1-train.csv')

population = []
for index in range(0, int(sys.argv[1])):
    print(index)
    population.append(Individual(index))
    population[index].root.print_tree()

fit = fitness.Fitness(dataHolder.train)
#fit.calculate(ind.root)
print(eval('((0.804694852981791)**(((math.cos(math.log((250)**(15.142228210831043))))+(math.sqrt(math.sin((76.3139001845522)/(11.011117825660167)))))*(91.99716498921566)))'))
