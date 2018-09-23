#!/usr/bin/python3

import sys
import libs.tree as tree
import libs.data as data

class Individual:
    def __init__(self, fitnessObject, number_of_variables, tree=None, random_seed=None):
        if not tree:
            self.tree = self.generateRandomTree(number_of_variables, random_seed)
        else:
            self.tree = tree
        self.root = self.tree.root
        self.fitness = self.calculateFitness(fitnessObject)

    def generateRandomTree(self, number_of_variables, random_seed=None, tree_max_depth=7):
        return tree.RandomTree(number_of_variables, random_seed, tree_max_depth)

    def calculateFitness(self, fitnessObject):
        return fitnessObject.calculate(self.root)
