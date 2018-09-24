#!/usr/bin/python3

import math
import numpy as np

class Tournament:
    def __init__(self, k, randomSeed=None):
        if randomSeed:
            np.random.seed(randomSeed)

        self.k = k

    def execute(self, population):
        if self.k > len(population):
            self.k = len(population)
        
        nTournaments = math.ceil(len(population) / self.k)
        tournament = self.split_population_into_tournaments(population, nTournaments)

        newPopulation = list(map(lambda x: get_best_individual(x), tournament))

        return newPopulation

    def split_population_into_tournaments(self, population, nTour):
        population = population.copy()
        initialPopulationLen = len(population)
        tournaments = [[] for _ in range(nTour)]

        for _ in range(initialPopulationLen):
            tourIndex = np.random.randint(nTour)

            if len(tournaments[tourIndex]) >= self.k:
                tourIndex = 0
                while len(tournaments[tourIndex]) >= self.k:
                    tourIndex += 1

            popIndex = np.random.randint(len(population))
            tournaments[tourIndex].append(population[popIndex])
            population.pop(popIndex)

        return tournaments

def get_best_individual(population):
    bestInd = min(population, key=lambda x: x.fitness)
    return bestInd
