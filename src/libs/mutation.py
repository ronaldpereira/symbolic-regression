#!/usr/bin/python3

import numpy as np
import libs.tree as tree

class Mutation:
    def __init__(self, prob, random_seed=None):
        if random_seed:
            np.random.seed(random_seed)

        self.prob = prob

    def execute(self, mutation_father):
        if np.random.rand() <= self.prob:
            subtree_root = mutation_father.root.get_random_node()
            subtree_father, direction = mutation_father.root.get_node_father(subtree_root)
            new_randon_subtree = tree.RandomTree(mutation_father.max_variables, max_depth=subtree_root.get_subtree_height())

            if subtree_father:
                if direction:
                    subtree_father.insert_subtree(new_randon_subtree.root, direction)
                else:
                    mutation_father = new_randon_subtree

            return mutation_father

        return None
        
