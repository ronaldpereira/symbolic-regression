#!/usr/bin/python3

import math
import copy

class BestIndividual:
    def __init__(self):
        self.individual = None
        self.fitness = math.inf

    def check_best_individual(self, newInd):
        if newInd.fitness < self.fitness:
            self.individual = copy.deepcopy(newInd)
            self.fitness = self.individual.fitness

    def get_best_individual(self):
        return self.individual
