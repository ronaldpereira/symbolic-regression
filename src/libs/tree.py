#!/usr/bin/python3

import numpy as np
from io import StringIO
import sys

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.childNumber = 0
        self.data = None

    def insert(self, data, n_child=0):
        self.data = data

        if n_child == 1:
            self.childNumber = 1
            self.right = Node()
        elif n_child == 2:
            self.childNumber = 2
            self.left = Node()
            self.right = Node()

    def insert_subtree(self, subtree, direction):
        if direction == 'l':
            self.left = subtree
        elif direction == 'r':
            self.right = subtree

    def get_tree(self):
        print('(', end='')
        if self.left:
            self.left.get_tree()
        if self.data:
            print(self.data, end='')
        if self.right:
            self.right.get_tree()
        print(')', end='')

    def print_tree(self):
        # It changes the stdout to be stored on the tree variable and then restore it to stdout
        old_stdout = sys.stdout
        tree = StringIO()
        sys.stdout = tree

        self.get_tree()

        sys.stdout = old_stdout

        return tree.getvalue()

    def subtree_recursive_counter(self, size=1):
        if self.left:
            size += self.left.subtree_recursive_counter()
        if self.right:
            size += self.right.subtree_recursive_counter()

        return size

    def get_subtree_size(self, size=0):
        if self.data:
            size = self.subtree_recursive_counter()

        return size

    def get_subtree_height(self):
        if not self.data:
            return -1

        if self.left:
            left = self.left.get_subtree_height()
        else:
            left = -1

        if self.right:
            right = self.right.get_subtree_height()
        else:
            right = -1

        return 1 + max(left, right)

    def get_random_node(self):
        left_size = 0 if not self.left else self.left.get_subtree_size()

        if left_size > 0:
            index = np.random.randint(2*left_size)

            if index < left_size:
                return self.left.get_random_node()
            elif index == left_size:
                return self
            else:
                return self.right.get_random_node()

        else:
            return self

    def get_node_father(self, node=None):
        if node:
            if self == node:
                return self, None
            else:
                if self.left:
                    if self.left == node:
                        return self, 'l'
                    else:
                        return self.left.get_node_father(node)
                if self.right:
                    if self.right == node:
                        return self, 'r'
                    else:
                        return self.right.get_node_father(node)

        return None, None


class RandomTree:
    def __init__(self, max_variables, random_seed=None, max_depth=7):
        if random_seed:
            np.random.seed(random_seed)

        self.max_depth = max_depth
        self.max_variables = max_variables

        if max_depth > 0:
            self.root = self.generate_node()

            if self.root.childNumber == 1:
                self.root.right = self.generate_subtree(self.root.right)
            elif self.root.childNumber == 2:
                self.root.left = self.generate_subtree(self.root.left)
                self.root.right = self.generate_subtree(self.root.right)

        else:
            self.root = self.generate_node(True)

    def generate_subtree(self, node, actualDepth=1):
        actualDepth += 1
        node = self.generate_node(actualDepth >= self.max_depth)

        if node.childNumber == 1:
            node.right = self.generate_subtree(node.right, actualDepth)
        elif node.childNumber == 2:
            node.left = self.generate_subtree(node.left, actualDepth)
            node.right = self.generate_subtree(node.right, actualDepth)

        return node

    def generate_node(self, justTerminal=False):
        node = Node()

        if not justTerminal:
            data, n_child = self.random_function_call()
        else:
            data, n_child = self.get_terminal()

        node.insert(data, n_child)
        return node

    def random_function_call(self):
        function_list = [self.get_binary_function, self.get_unary_function, self.get_terminal]

        return function_list[np.random.randint(0, len(function_list))]()

    def get_binary_function(self):
        binary_function_list = ['+', '-', '*', '/prot_math.div', '**prot_math.pow']

        return binary_function_list[np.random.randint(0, len(binary_function_list))], 2

    def get_unary_function(self):
        unary_function_list = ['prot_math.sqrt', 'math.sin', 'math.cos', 'prot_math.log', 'prot_math.log2', 'prot_math.log10']

        return unary_function_list[np.random.randint(0, len(unary_function_list))], 1

    def get_terminal(self):
        random = np.random.rand()

        if random < 0.5:
            # returns variable Xi terminal
            return 'X[' + str(np.random.randint(0, self.max_variables)) + ']', 0
        else:
            # returns random constant
            return np.random.uniform(-100, 100), 0
