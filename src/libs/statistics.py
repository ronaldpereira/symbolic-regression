#!/usr/bin/python3

import math
from collections import Counter

class Statistics:
    def __init__(self):
        self.n_best_crossover_child = 0
        self.n_worse_crossover_child = 0
        self.n_repeated_individuals = 0

    def get_train_statistics(self, population, train):
        self.population = population
        self.train = train

        self.best_individual_fitness()
        self.worst_individual_fitness()
        self.mean_fitness()
        self.get_crossover_best_and_worse()
        self.get_repeated_individuals()
    
    def get_test_statistics(self, population):
        self.population = population
        self.best_individual_test()

    def best_individual_fitness(self):
        best_ind = min(self.population, key=lambda x: x.fitness)
        print('Best Individual Fitness:', best_ind.fitness)

    def worst_individual_fitness(self):
        worst_ind = max(self.population, key=lambda x: x.fitness)
        print('Worst Individual Fitness:', worst_ind.fitness)

    def mean_fitness(self):
        total_fitness = 0
        for individual in self.population:
            total_fitness += individual.fitness
        print('Mean Fitness:', total_fitness / len(self.population))

    def set_crossover_best_and_worse(self, crossover_population):
        fathers_mean = (crossover_population[0].fitness + crossover_population[1].fitness) / 2

        if crossover_population[2].fitness < fathers_mean:
            self.n_best_crossover_child += 1
        elif crossover_population[2].fitness > fathers_mean:
            self.n_worse_crossover_child += 1

        if crossover_population[3].fitness < fathers_mean:
            self.n_best_crossover_child += 1
        elif crossover_population[3].fitness > fathers_mean:
            self.n_worse_crossover_child += 1

    def get_crossover_best_and_worse(self):
        print('Crossover child worse than father\'s mean:', self.n_worse_crossover_child)
        print('Crossover child better than father\'s mean:', self.n_best_crossover_child)
        
    def set_repeated_individuals(self):
        counted = [0]*len(self.population)
        for index1 in range(len(self.population)):
            for index2 in range(index1+1, len(self.population)):
                if self.population[index1].root.print_tree() == self.population[index2].root.print_tree():
                    if counted[index1] == 0 and counted[index2] == 0:
                        counted[index1] = 1
                        counted[index2] = 1
                        self.n_repeated_individuals += 2
                    elif counted[index2] == 0:
                        counted[index2] = 1
                        self.n_repeated_individuals += 1

    def get_repeated_individuals(self):
        self.set_repeated_individuals()
        print('Repeated individuals:', self.n_repeated_individuals)

    def best_individual_test(self):
        print('\n***TEST STATISTICS***')
        best_ind = min(self.population, key=lambda x: x.fitness)
        print('Best Individual:')
        print(best_ind.root.print_tree())
        print('Best Individual Train Fitness:', best_ind.fitness)
        best_ind.calculate_test_fitness()
        print('Best Individual Test Fitness:', best_ind.test_fitness)
