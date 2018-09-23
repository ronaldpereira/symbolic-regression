#!/usr/bin/python3

import sys
import libs.data as data
import libs.tree as tree
import libs.fitness as fitness
import libs.statistics as statistics
import libs.mutation as mutation
import libs.crossover as crossover

population_size = int(sys.argv[1])
tree_max_depth = 7

class Individual:
    def __init__(self, randomSeed=None):
        self.tree = self.generateRandomTree(randomSeed)
        self.root = self.tree.root

    def generateRandomTree(self, randomSeed=None):
        return tree.RandomTree(dataHolder.numberOfVariables, randomSeed, tree_max_depth)

    def calculateFitness(self, fitness):
        self.fitness = fitness.calculate(self.root)


dataHolder = data.Data('./input/datasets/synth1/synth1-train.csv')

fit = fitness.Fitness(dataHolder.train)

population = []
for index in range(0, population_size):
    population.append(Individual(index))
    population[index].calculateFitness(fit)

print(population[1].root.print_tree())
print(population[1].root.get_subtree_height())
print()
print(population[15].root.print_tree())
print(population[15].root.get_subtree_height())
print()
cross = crossover.Crossover(0.9, 15)
random_node1, random_node2 = cross.execute(population[1].tree, population[15].tree)
if random_node1 and random_node2:
    print(random_node1.root.print_tree())
    print(random_node1.root.get_subtree_height())
    print()
    print(random_node2.root.print_tree())
    print(random_node2.root.get_subtree_height())

#statistics.get_statistics(population)
