#!/usr/bin/python3

import numpy as np

class Crossover:
    def __init__(self, prob, random_seed=None):
        if random_seed:
            np.random.seed(random_seed)

        self.prob = prob

    def execute(self, crossover1, crossover2):

        if np.random.rand() <= self.prob:
            # Tries to crossover 2 trees 50 times, if it fails, returns primitive fathers
            for i in range(50):
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
                        return crossover1, crossover2
        
        return None, None
