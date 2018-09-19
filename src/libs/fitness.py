#!/usr/bin/python3

import pandas as pd
import numpy as np

class Fitness:
    def __init__(self, trainDF):
        self.train = trainDF.copy()

    def calculate(self, treeRoot):
        y_mean = self.train['Y'].mean()
        trainLen = len(self.train)

        sum_of_squares = 0
        normalize = 0
        for index in range(trainLen):
            sum_of_squares += (self.train.loc[index, 'Y'] - self.evaluate_individual(treeRoot)) ** 2
            normalize += (self.train.loc[index, 'Y'] - y_mean) ** 2

        return np.sqrt(sum_of_squares / normalize)

    def evaluate_individual(self, treeRoot):
        # Need to replace X[i] with data value and eval individual
        return 0
