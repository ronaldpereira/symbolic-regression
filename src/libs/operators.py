#!/usr/bin/python3

import copy
import numpy as np
import libs.individual as individual
import libs.tree as tree

class Operators:
    def __init__(self, population, desiredPopulationSize, mutationProb, crossoverProb, nVariables, fitnessObject, statisticsObject, activateElitistOperators):
        self.population = population
        self.desiredPopulationSize = desiredPopulationSize
        self.mutationProb = mutationProb
        self.crossoverProb = crossoverProb
        self.reproductionProb = 1.0 - self.mutationProb - self.crossoverProb
        self.nVariables = nVariables
        self.fitnessObject = fitnessObject
        self.statisticsObject = statisticsObject
        self.activateElitistOperators = activateElitistOperators

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
                    self.population.append(Mutation.mutate_individual(ind, self.fitnessObject, self.nVariables, self.activateElitistOperators))

                # If the random number [0, 1) is in the crossover probability (mutation + crossover probabilities), then do it on 2 random individuals from population
                elif random < self.mutationProb + self.crossoverProb:
                    ind1 = copy.copy(self.population[np.random.randint(len(self.population))])
                    ind2 = copy.copy(self.population[np.random.randint(len(self.population))])
                    self.population.extend(Crossover.crossover_individuals(ind1, ind2, self.fitnessObject, self.nVariables, self.statisticsObject, self.activateElitistOperators))
                
                # If the random number [0,1) isn't in the mutation nor the crossover probability, then just reproduce the individual into new population
                else:
                    ind = copy.deepcopy(self.population[np.random.randint(len(self.population))])
                    self.population.append(ind)

        return self.population

class Mutation:
    @staticmethod
    def mutate_individual(ind, fitnessObject, nVariables, elit):
        father = copy.deepcopy(ind)

        mutatedTree = Mutation.execute(copy.deepcopy(ind.tree))
        mutatedInd = individual.Individual(fitnessObject, nVariables, mutatedTree)

        # Returns only the individual with the best fitness
        if elit:
            return min([father, mutatedInd], key=lambda x: x.fitness)
        else:
            return mutatedInd

    @staticmethod
    def execute(mutationTree):
        # Tries to mutate a tree 50 times, if it fails, returns primitive father
        for _ in range(50):
            subtree_root = mutationTree.root.get_random_node()
            subtree_father, direction = mutationTree.root.get_node_father(subtree_root)
            new_random_subtree = tree.RandomTree(mutationTree.maxVariables, method='grow', maxDepth=mutationTree.root.get_subtree_height())

            if subtree_father:
                if direction:
                    subtree_father.insert_subtree(new_random_subtree.root, direction)
                else:
                    mutationTree = new_random_subtree
                if mutationTree.root.get_subtree_height() <= mutationTree.maxDepth:
                    break

        return mutationTree

class Crossover:
    @staticmethod
    def crossover_individuals(ind1, ind2, fitnessObject, nVariables, stats, elit):
        father1 = copy.deepcopy(ind1)
        father2 = copy.deepcopy(ind2)

        crossover_tree1, crossover_tree2 = Crossover.execute(copy.deepcopy(ind1.tree), copy.deepcopy(ind2.tree))
        crossover_ind1 = individual.Individual(fitnessObject, nVariables, crossover_tree1)
        crossover_ind2 = individual.Individual(fitnessObject, nVariables, crossover_tree2)

        crossover_population = [father1, father2, crossover_ind1, crossover_ind2]
        stats.set_crossover_best_and_worse(crossover_population)

        if elit:
            crossover_population.sort(key=lambda x: x.fitness)
            return [crossover_population[0], crossover_population[1]]
        else:
            return [crossover_ind1, crossover_ind2]

    @staticmethod
    def execute(crossover1, crossover2):
        # Tries to crossover 2 trees 50 times, if it fails, returns primitive fathers
        for _ in range(50):
            subtreeRoot1 = crossover1.root.get_random_node()
            subtreeRoot2 = crossover2.root.get_random_node()

            subtreeFather1, direction1 = crossover1.root.get_node_father(subtreeRoot1)
            subtreeFather2, direction2 = crossover2.root.get_node_father(subtreeRoot2)

            if subtreeFather1 and subtreeFather2:
                if direction1 and direction2:
                    subtreeFather1.insert_subtree(subtreeRoot2, direction1)
                    subtreeFather2.insert_subtree(subtreeRoot1, direction2)
                elif direction1:
                    subtreeFather1.insert_subtree(subtreeRoot2, direction1)
                    crossover2.root = subtreeRoot1
                elif direction2:
                    crossover1.root = subtreeRoot2
                    subtreeFather2.insert_subtree(subtreeRoot1, direction2)
                else:
                    crossover1.root = subtreeRoot2
                    crossover2.root = subtreeRoot1

                if crossover1.root.get_subtree_height() <= crossover1.maxDepth and crossover2.root.get_subtree_height() <= crossover2.maxDepth:
                    break
        
        return crossover1, crossover2


