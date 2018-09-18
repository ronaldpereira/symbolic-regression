#!/usr/bin/python3

import tree
import sys
import fitness

treeMaxDepth = 7

class Individual:
    def __init__(self):
        self.tree = self.generateRandomTree()

    def generateRandomTree(self):
        pass


root = tree.Node('+')
root.insert(5, 'l')
root.insert('-', 'r')
root.right.insert(9, 'l')
root.right.insert(3, 'r')
root.print_subtree()
print(end='\n\n')

fit = fitness.Fitness('./input/datasets/synth1/synth1-train.csv')
fit.calculate(root)
fit = fitness.Fitness('./input/datasets/concrete/concrete-train.csv')
fit.calculate(root)
