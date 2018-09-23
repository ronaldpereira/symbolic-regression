#!/usr/bin/python3

import numpy as np
import libs.tree as tree
import libs.individual as individual

class Mutation:
    def __init__(self, prob, number_of_variables, random_seed=None):
        if random_seed:
            np.random.seed(random_seed)

        self.number_of_variables = number_of_variables
        self.prob = prob

    def mutate_population(self, population, fit, ):
        for index in range(len(population)):
            if np.random.rand() <= self.prob:
                mutated_tree = self.execute(population[index].tree)
                mutated_ind = individual.Individual(fit, self.number_of_variables, mutated_tree)

                if mutated_ind.fitness < population[index].fitness:
                    population[index] = mutated_ind

        return population

    def execute(self, mutation_tree):
        # Tries to mutate a tree 50 times, if it fails, returns primitive father
        for _ in range(50):
            subtree_root = mutation_tree.root.get_random_node()
            subtree_father, direction = mutation_tree.root.get_node_father(subtree_root)
            new_randon_subtree = tree.RandomTree(mutation_tree.max_variables, max_depth=mutation_tree.root.get_subtree_height())

            if subtree_father:
                if direction:
                    subtree_father.insert_subtree(new_randon_subtree.root, direction)
                else:
                    mutation_tree = new_randon_subtree
                if mutation_tree.root.get_subtree_height() <= mutation_tree.max_depth:
                    break

        return mutation_tree
