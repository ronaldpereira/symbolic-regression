#!/usr/bin/python3

import math
import numpy as np

class Tournament:
    def __init__(self, k):
        self.k = k

    def execute(self, population):
        newPopulation = []

        if self.k > len(population):
            self.k = len(population)

        tournamentWinner = self.tournament(population)

        # Add the current tournament winner to the new population
        newPopulation.append(tournamentWinner)

        return newPopulation

    def tournament(self, population):
        tournament = []
        for _ in range(self.k):
            tournament.append(population[np.random.randint(len(population))])

        return get_best_individual(tournament)


def get_best_individual(population):
    return min(population, key=lambda x: x.fitness)
