#!/usr/bin/python3

import math
import numpy as np
import libs.individual as individual
import libs.tree as tree

class Operands:
    def __init__(self, population, desiredPopulationSize, mutationProb, crossoverProb, nVariables, fitnessObject, statisticsObject, randomSeed=None):
        if randomSeed:
            np.random.seed(randomSeed)

        self.population = population
        self.desiredPopulationSize = desiredPopulationSize
        self.mutationProb = mutationProb
        self.crossoverProb = crossoverProb
        self.reproductionProb = 1.0 - self.mutationProb - self.crossoverProb
        self.nVariables = nVariables
        self.fitnessObject = fitnessObject
        self.statisticsObject = statisticsObject

    def execute(self):
        while True:
            if len(self.population) == self.desiredPopulationSize:
                break

            elif len(self.population) > self.desiredPopulationSize:
                individualsToBeRemoved = len(self.population) - self.desiredPopulationSize
                self.population = self.population[:-individualsToBeRemoved]

            else:
                random = np.random.uniform()

                # If the random number [0,1) is under the mutation probability, then do mutation on a random individual from population
                if random < self.mutationProb:
                    ind = self.population[np.random.randint(len(self.population))]
                    self.population.append(Mutation.mutate_individual(ind, self.fitnessObject, self.nVariables))

                # If the random number [0, 1) is in the crossover probability (mutation + crossover probabilities), then do it on 2 random individuals from population
                elif random < self.mutationProb + self.crossoverProb:
                    ind1 = self.population[np.random.randint(len(self.population))]
                    ind2 = self.population[np.random.randint(len(self.population))]
                    self.population.extend(Crossover.crossover_individuals(ind1, ind2, self.fitnessObject, self.nVariables, self.statisticsObject))
                
                # If the random number [0,1) isn't in the mutation nor the crossover probability, then just reproduce the individual into new population
                else:
                    ind = self.population[np.random.randint(len(self.population))]
                    self.population.append(ind)
        print(list(map(lambda x: x.root.print_tree(), self.population)))
        return self.population

class Mutation:
    @staticmethod
    def mutate_individual(ind, fitnessObject, nVariables):
        father = ind

        mutatedTree = Mutation.execute(ind.tree)
        mutatedInd = individual.Individual(fitnessObject, nVariables, mutatedTree)

        # Returns only the individual with the best fitness
        return min([father, mutatedInd], key=lambda x: x.fitness)

    @staticmethod
    def execute(mutationTree):
        # Tries to mutate a tree 50 times, if it fails, returns primitive father
        for _ in range(50):
            subtree_root = mutationTree.root.get_random_node()
            subtree_father, direction = mutationTree.root.get_node_father(subtree_root)
            new_randon_subtree = tree.RandomTree(mutationTree.maxVariables, maxDepth=mutationTree.root.get_subtree_height())

            if subtree_father:
                if direction:
                    subtree_father.insert_subtree(new_randon_subtree.root, direction)
                else:
                    mutationTree = new_randon_subtree
                if mutationTree.root.get_subtree_height() <= mutationTree.maxDepth:
                    break

        return mutationTree

class Crossover:
    @staticmethod
    def crossover_individuals(ind1, ind2, fitnessObject, nVariables, stats):
        father1 = ind1
        father2 = ind2

        crossover_tree1, crossover_tree2 = Crossover.execute(ind1.tree, ind2.tree)
        crossover_ind1 = individual.Individual(fitnessObject, nVariables, crossover_tree1)
        crossover_ind2 = individual.Individual(fitnessObject, nVariables, crossover_tree2)

        crossover_population = [father1, father2, crossover_ind1, crossover_ind2]
        stats.set_crossover_best_and_worse(crossover_population)
        crossover_population.sort(key=lambda x: x.fitness)

        return [crossover_population[0], crossover_population[1]]

    @staticmethod
    def execute(crossover1, crossover2):
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


