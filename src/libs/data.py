#!/usr/bin/python3

import numpy as np
import pandas as pd

class Data:
    def __init__(self, trainCSVPath='', testCSVPath=''):
        if trainCSVPath != '':
            self.train = pd.read_csv(trainCSVPath, header=None)

            header = ['X[' + str(i) + ']' for i in range(0, len(self.train.iloc[0]) - 1)] + ['Y']
            self.train.columns = header

        if testCSVPath != '':
            self.test = pd.read_csv(testCSVPath, header=None)

            header = ['X[' + str(i) + ']' for i in range(0, len(self.test.iloc[0]) - 1)] + ['Y']
            self.test.columns = header

        if not self.train.empty:
            self.nVariables = len(self.train.iloc[0]) - 1
