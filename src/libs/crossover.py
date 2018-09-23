#!/usr/bin/python3

import numpy as np

class Crossover:
    def __init__(self, prob, random_seed=None):
        if random_seed:
            np.random.seed(random_seed)

        self.prob = prob

    def execute(self, rootNode1, rootNode2):
        if np.random.rand() <= self.prob:
            pass
        else:
            return None
