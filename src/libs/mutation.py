#!/usr/bin/python3

import numpy as np
import libs.tree as tree

class Mutation:
    def __init__(self, prob, random_seed=None):
        if random_seed:
            np.random.seed(random_seed)

        self.prob = prob

    def execute(self, mutation_tree):
        if np.random.rand() <= self.prob:
            subtree_root_node = mutation_tree.root.get_random_node()
            subtree_father, direction = mutation_tree.root.get_node_father(subtree_root_node)
            new_subtree = tree.RandomTree(mutation_tree.max_variables, max_depth=subtree_root_node.get_subtree_height())

            if subtree_father:
                if direction == 'l' or direction == 'r':
                    subtree_father.insert_subtree(new_subtree.root, direction)
                else:
                    mutation_tree = new_subtree

        return mutation_tree
        
