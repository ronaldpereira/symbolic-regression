#!/usr/bin/python3

import pandas as pd
import numpy as np
import math
import libs.protected_math_functions as prot_math

import warnings
warnings.filterwarnings('ignore')

class Fitness:
    def __init__(self, trainDF, testDF):
        self.train = trainDF.copy()
        self.test = testDF.copy()

    def calculate_train(self, treeRoot):
        yMean = self.train['Y'].mean()
        trainLen = len(self.train)

        sumOfSquares = 0
        normalize = 0
        for index in range(trainLen):
            try:
                evalInd = self.evaluate_individual(treeRoot, index)

                sumOfSquares += (self.train.loc[index, 'Y'] - evalInd) ** 2
            except:
                sumOfSquares = math.inf

            normalize += (self.train.loc[index, 'Y'] - yMean) ** 2

        trainFitness = np.sqrt(sumOfSquares / normalize)
        return trainFitness

    def calculate_test(self, treeRoot):
        yMean = self.test['Y'].mean()
        testLen = len(self.test)

        sumOfSquares = 0
        normalize = 0
        for index in range(testLen):
            try:
                evalInd = self.evaluate_individual(treeRoot, index, train=False)

                sumOfSquares += (self.test.loc[index, 'Y'] - evalInd) ** 2
            except:
                sumOfSquares = math.inf

            normalize += (self.test.loc[index, 'Y'] - yMean) ** 2

        testFitness = np.sqrt(sumOfSquares / normalize)
        return testFitness

    def evaluate_individual(self, treeRoot, index, train=True):
        if train:
            X = self.train.iloc[index, :-1]
        else:
            X = self.test.iloc[index, :-1]

        return eval(str(treeRoot.print_tree()))
