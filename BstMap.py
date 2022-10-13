from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key, value):
        '''Inserts a new node as a left/right child of a leaf node'''
        if key == self.key:
            self.value = value
        elif key > self.key:
            if self.right is not None:
                self.right.put(key, value)
            else:
                self.right = Node(key, value, None, None)
        else:
            if self.left is not None:
                self.left.put(key, value)
            else:
                self.left = Node(key, value, None, None)

    def to_string(self):
        '''Traverses the tree and returns a string of the key:value pair
        recursively'''
        ret_str = ""
        if self.left is not None:
            ret_str += self.left.to_string()
        # Returning the string in alphabetical order
        ret_str += f"({self.key}, {self.value}) "
        if self.right is not None:
            ret_str += self.right.to_string()
        return ret_str

    def count(self):
        '''Traverses the tree and returns the amount of nodes'''
        # Start at 1 to count the root
        count = 1
        if self.left is not None:
            count += self.left.count()
        if self.right is not None:
            count += self.right.count()
        return count       # Placeholder code ==> to be replaced

    def get(self, key):
        if self.key == key:
            return self.value
        elif self.key < key:
            if self.right is not None:
                return self.right.get(key)
        else:
            if self.left is not None:
                return self.left.get(key)


    def max_depth(self):
        pass     # Placeholder code ==> to be replaced

    def count_leafs(self):
        pass     # Placeholder code ==> to be replaced

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        return [None]    # Placeholder code to avoid crash in demo program. To be replaced


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a leaf node count. That is, the number of nodes 
    # with no children
    def count_leafs(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
