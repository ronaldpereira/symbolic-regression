#!/usr/bin/python3

import math
import numpy as np
import libs.individual as individual
import libs.statistics as statistics

class Crossover:
    def __init__(self, prob, numberOfVariables, randomSeed=None):
        if randomSeed:
            np.random.seed(randomSeed)

        self.numberOfVariables = numberOfVariables
        self.prob = prob

    def cross_population(self, population, fitnessObject, stats):
        nPossibleCrossovers = math.floor(len(population) / 2)
        for _ in range(nPossibleCrossovers):
            if np.random.rand() <= self.prob:
                index1 = np.random.randint(len(population))
                index2 = np.random.randint(len(population))
                crossover_tree1, crossover_tree2 = self.execute(population[index1].tree, population[index2].tree)

                crossover_ind1 = individual.Individual(fitnessObject, self.numberOfVariables, crossover_tree1)
                crossover_ind2 = individual.Individual(fitnessObject, self.numberOfVariables, crossover_tree2)

                crossover_population = [population[index1], population[index2], crossover_ind1, crossover_ind2]
                stats.set_crossover_best_and_worse(crossover_population)
                crossover_population.sort(key=lambda x: x.fitness)

                population[index1] = crossover_population[0]
                population[index2] = crossover_population[1]

        return population

    def execute(self, crossover1, crossover2):
        # Tries to crossover 2 trees 50 times, if it fails, returns primitive fathers
        for _ in range(50):
            subtreeRoot1 = crossover1.root.get_random_node()
            subtreeRoot2 = crossover2.root.get_random_node()
            subtreeRather1, direction1 = crossover1.root.get_node_father(subtreeRoot1)
            subtreeRather2, direction2 = crossover2.root.get_node_father(subtreeRoot2)

            if subtreeRather1 and subtreeRather2:
                if direction1 and direction2:
                    subtreeRather1.insert_subtree(subtreeRoot2, direction1)
                    subtreeRather2.insert_subtree(subtreeRoot1, direction2)
                elif direction1:
                    subtreeRather1.insert_subtree(subtreeRoot2, direction1)
                    crossover2.root = subtreeRoot1
                elif direction2:
                    crossover1.root = subtreeRoot2
                    subtreeRather2.insert_subtree(subtreeRoot1, direction2)
                else:
                    crossover1.root = subtreeRoot2
                    crossover2.root = subtreeRoot1

                if crossover1.root.get_subtree_height() <= crossover1.maxDepth and crossover2.root.get_subtree_height() <= crossover2.maxDepth:
                    break
        
        return crossover1, crossover2
