#!/usr/bin/python3

import numpy as np
import libs.tree as tree
import libs.individual as individual

class Mutation:
    def __init__(self, prob, numberOfVariables, activateElitism=True, randomSeed=None):
        if randomSeed:
            np.random.seed(randomSeed)

        self.numberOfVariables = numberOfVariables
        self.prob = prob
        self.activateElitism = activateElitism

    def mutate_population(self, population, fit, ):
        for index in range(len(population)):
            if np.random.rand() <= self.prob:
                mutatedTree = self.execute(population[index].tree)
                mutated_ind = individual.Individual(fit, self.numberOfVariables, mutatedTree)

                # If elitism is activated, then the best individual will continue
                if self.activateElitism:
                    if mutated_ind.fitness < population[index].fitness:
                        population[index] = mutated_ind
                # If elitism is deactivated, then the child will always substitute his father
                else:
                    population[index] = mutated_ind


        return population

    def execute(self, mutationTree):
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
