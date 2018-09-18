#!/usr/bin/python3
import math
import tree

class Individual:
    
    def __init__(self):
        pass

root = tree.Node('+')
root.insert(5, 'l')
root.insert(4, 'r')
root.print_subtree()
