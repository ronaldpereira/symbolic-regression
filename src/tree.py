#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data, child='l'):
        if child == 'l':
            self.left = Node(data)
        elif child == 'r':
            self.right = Node(data)

    def print_subtree(self):
        if self.left:
            self.left.print_subtree()

        print(self.data)
        
        if self.right:
            self.right.print_subtree()
