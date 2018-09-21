#!/usr/bin/python3

import pandas as pd
import numpy as np
import math
import libs.protected_math_functions as prot_math

import warnings
warnings.filterwarnings('ignore')

class Fitness:
    def __init__(self, trainDF):
        self.train = trainDF.copy()

    def calculate(self, treeRoot):
        y_mean = self.train['Y'].mean()
        trainLen = len(self.train)

        sum_of_squares = 0
        normalize = 0
        for index in range(trainLen):
            try:
                eval_ind = self.evaluate_individual(treeRoot, index)

                if type(eval_ind) == int or type(eval_ind) == float:
                    sum_of_squares += (self.train.loc[index, 'Y'] - eval_ind) ** 2
                else:
                    sum_of_squares += math.inf
            except:
                sum_of_squares = math.inf

            normalize += (self.train.loc[index, 'Y'] - y_mean) ** 2

        fitness = np.sqrt(sum_of_squares / normalize)
        return fitness

    def evaluate_individual(self, treeRoot, index):
        X = self.train.iloc[index, :-1]
        return eval(str(treeRoot.print_tree()))
