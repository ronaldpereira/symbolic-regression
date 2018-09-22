#!/usr/bin/python3

import numpy as np

class Mutation:
    def __init__(self, prob):
        self.prob = prob

    def execute(self, rootNode):
        if np.random.rand() <= self.prob:
            pass
        else:
            return rootNode

    def get_random_subtree(self, rootNode):
        rootNode.get_random_node()
        
