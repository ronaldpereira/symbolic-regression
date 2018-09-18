#!/usr/bin/python3

import numpy as np

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
    def generate(randomSeed=0, maxDepth=7):
        np.random.seed(randomSeed)

                    

    @staticmethod
    def getBinaryNonTerminal():
        binNonTerminalList = ['add', '-', '*', '/', '^']


    @staticmethod
    def getUnaryNonTerminal():
        unNonTerminalList = ['sqrt', 'sin', 'cos']

