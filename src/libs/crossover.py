#!/usr/bin/python3

import math
import numpy as np
import libs.individual as individual
import libs.statistics as statistics

class Crossover:
    def __init__(self, prob, number_of_variables, random_seed=None):
        if random_seed:
            np.random.seed(random_seed)

        self.number_of_variables = number_of_variables
        self.prob = prob

    def cross_population(self, population, fit, stats):
        n_possible_crossovers = math.floor(len(population) / 2)
        for _ in range(n_possible_crossovers):
            if np.random.rand() <= self.prob:
                index1 = np.random.randint(len(population))
                index2 = np.random.randint(len(population))
                crossover_tree1, crossover_tree2 = self.execute(population[index1].tree, population[index2].tree)

                crossover_ind1 = individual.Individual(fit, self.number_of_variables, crossover_tree1)
                crossover_ind2 = individual.Individual(fit, self.number_of_variables, crossover_tree2)

                crossover_population = [population[index1], population[index2], crossover_ind1, crossover_ind2]
                stats.set_crossover_best_and_worse(crossover_population)
                crossover_population.sort(key=lambda x: x.fitness)

                population[index1] = crossover_population[0]
                population[index2] = crossover_population[1]

        return population

    def execute(self, crossover1, crossover2):
        # Tries to crossover 2 trees 50 times, if it fails, returns primitive fathers
        for _ in range(50):
            subtree_root1 = crossover1.root.get_random_node()
            subtree_root2 = crossover2.root.get_random_node()
            subtree_father1, direction1 = crossover1.root.get_node_father(subtree_root1)
            subtree_father2, direction2 = crossover2.root.get_node_father(subtree_root2)

            if subtree_father1 and subtree_father2:
                if direction1 and direction2:
                    subtree_father1.insert_subtree(subtree_root2, direction1)
                    subtree_father2.insert_subtree(subtree_root1, direction2)
                elif direction1:
                    subtree_father1.insert_subtree(subtree_root2, direction1)
                    crossover2.root = subtree_root1
                elif direction2:
                    crossover1.root = subtree_root2
                    subtree_father2.insert_subtree(subtree_root1, direction2)
                else:
                    crossover1.root = subtree_root2
                    crossover2.root = subtree_root1

                if crossover1.root.get_subtree_height() <= crossover1.max_depth and crossover2.root.get_subtree_height() <= crossover2.max_depth:
                    break
        
        return crossover1, crossover2
