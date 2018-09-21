#!/usr/bin/python3

import numpy as np
from io import StringIO
import sys

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.childNumber = 0
        self.data = None

    def insert(self, data, n_child=0):
        self.data = data

        if n_child == 1:
            self.childNumber = 1
            self.right = Node()
        elif n_child == 2:
            self.childNumber = 2
            self.left = Node()
            self.right = Node()

    def get_tree(self):
        print('(', end='')
        if self.left:
            self.left.get_tree()

        if(self.data is not None):
            print(self.data, end='')

        if self.right:
            self.right.get_tree()
        print(')', end='')

    def print_tree(self):
        # It changes the stdout to be stored on the tree variable and then restore it to stdout
        old_stdout = sys.stdout
        tree = StringIO()
        sys.stdout = tree

        self.get_tree()

        sys.stdout = old_stdout

        return tree.getvalue()


class RandomTree:
    def __init__(self, maxNumberVariables, randomSeed=None, maxDepth=7):
        if randomSeed is not None:
            np.random.seed(randomSeed)

        self.maxDepth = maxDepth
        self.maxNumberVariables = maxNumberVariables
        self.root = self.generate_node()

        if self.root.childNumber == 1:
            self.root.right = self.generate_subtree(self.root.right)
        elif self.root.childNumber == 2:
            self.root.left = self.generate_subtree(self.root.left)
            self.root.right = self.generate_subtree(self.root.right)

    def generate_subtree(self, node, actualDepth=1):
        actualDepth += 1
        node = self.generate_node(actualDepth == self.maxDepth)

        if node.childNumber == 1:
            node.right = self.generate_subtree(node.right, actualDepth)
        elif node.childNumber == 2:
            node.left = self.generate_subtree(node.left, actualDepth)
            node.right = self.generate_subtree(node.right, actualDepth)

        return node

    def generate_node(self, justTerminal=False):
        node = Node()

        if not justTerminal:
            data, n_child = self.random_function_call()
        else:
            data, n_child = self.get_terminal()

        node.insert(data, n_child)
        return node

    def random_function_call(self):
        functionList = [self.get_binary_function, self.get_unary_function, self.get_terminal]

        return functionList[np.random.randint(0, len(functionList))]()

    def get_binary_function(self):
        binaryFunctionList = ['+', '-', '*', '/prot_math.div', '**prot_math.pow']

        return binaryFunctionList[np.random.randint(0, len(binaryFunctionList))], 2

    def get_unary_function(self):
        unaryFunctionList = ['prot_math.sqrt', 'math.sin', 'math.cos', 'prot_math.log', 'prot_math.log2', 'prot_math.log10']

        return unaryFunctionList[np.random.randint(0, len(unaryFunctionList))], 1

    def get_terminal(self):
        random = np.random.rand()

        if random < 0.5:
            # returns variable Xi terminal
            return 'X[' + str(np.random.randint(0, self.maxNumberVariables)) + ']', 0
        
        else:
            # returns random constant
            return np.random.uniform(-100, 100), 0
