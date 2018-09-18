#!/usr/bin/python3

import pandas as pd
import numpy as np

class Fitness:
    def __init__(self, trainCSVPath):
        if trainCSVPath != '':
            self.train = pd.read_csv(trainCSVPath, header=None)

            header = ['X' + str(i) for i in range(0, len(self.train.iloc[0]) - 1)] + ['Y']
            self.train.columns = header

    def calculate(self, treeRoot):
        y_mean = self.train['Y'].mean()
        trainLen = len(self.train)

        sum_of_squares = 0
        normalize = 0
        for index in range(trainLen):
            sum_of_squares += (self.train.loc[index, 'Y'] - self.evaluate_individual(treeRoot, self.train.drop('Y', axis=1).loc[index])) ** 2
            normalize += (self.train.loc[index, 'Y'] - y_mean) ** 2

        return np.sqrt(sum_of_squares / normalize)

    def evaluate_individual(self, treeRoot, features):
        return 0
