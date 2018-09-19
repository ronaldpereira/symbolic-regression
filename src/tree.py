#!/usr/bin/python3

import numpy as np

numberOfFeatures = 2

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data, child='l'):
        if child == 'l':
            self.left = Node(data)
        elif child == 'r':
            self.right = Node(data)

    def print_subtree(self):
        print('(', end='')
        if self.left:
            self.left.print_subtree()

        print(self.data, end='')
        
        if self.right:
            self.right.print_subtree()
        print(')', end='')


class RandomTree:
    @staticmethod
    def generate_child(randomSeed=0, maxDepth=7):
        np.random.seed(randomSeed)
        # must generate all node child within this class
                    

    @staticmethod
    def getBinaryFunction():
        binaryFunctionList = ['add', '-', '*', '/', '^']


    @staticmethod
    def getUnaryFunction():
        unaryFunctionList = ['sqrt', 'sin', 'cos']

    @staticmethod
    def getTerminal():
        random = np.random.randint(0, 10)

        if random < 5:
            #gets variable Xi terminal
            return 'X' + str(np.random.randint(0, numberOfFeatures))
        
        else:
            #gets random constant
            return np.random.uniform(-100, 100)

