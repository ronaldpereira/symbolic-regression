#!/usr/bin/python3

import math
import numpy as np

class Tournament:
    def __init__(self, k, random_seed=None):
        if random_seed:
            np.random.seed(random_seed)

        self.k = k

    def execute(self, population):
        if self.k > len(population):
            self.k = len(population)
        
        n_tournaments = math.ceil(len(population) / self.k)
        tournament = self.split_population_into_tournaments(population, n_tournaments)

        new_population = list(map(lambda x: get_best_individual(x), tournament))

        return new_population

    def split_population_into_tournaments(self, population, n_tour):
        population = population.copy()
        initial_population_len = len(population)
        tournaments = [[] for _ in range(n_tour)]

        for _ in range(initial_population_len):
            tour_index = np.random.randint(n_tour)

            if len(tournaments[tour_index]) >= self.k:
                tour_index = 0
                while len(tournaments[tour_index]) >= self.k:
                    tour_index += 1

            pop_index = np.random.randint(len(population))
            tournaments[tour_index].append(population[pop_index])
            population.pop(pop_index)

        return tournaments

def get_best_individual(population):
    best_ind = min(population, key=lambda x: x.fitness)
    return best_ind

