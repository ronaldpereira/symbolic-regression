#!/usr/bin/python3

import libs.tree as tree
import libs.data as data

class Individual:
    def __init__(self, fitnessObject, numberOfVariables, tree=None, method='grow'):
        if not tree:
            self.tree = self.generate_random_tree(numberOfVariables, method)
        else:
            self.tree = tree

        self.root = self.tree.root
        self.fitnessObject = fitnessObject
        self.fitness = self.calculate_train_fitness()

    def generate_random_tree(self, numberOfVariables, method, treeMaxDepth=7):
        return tree.RandomTree(numberOfVariables, method, treeMaxDepth)

    def calculate_train_fitness(self):
        return self.fitnessObject.calculate_train(self.root)

    def calculate_test_fitness(self):
        self.test_fitness = self.fitnessObject.calculate_test(self.root)
        return self.test_fitness
