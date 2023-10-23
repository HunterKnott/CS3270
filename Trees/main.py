'''Hunter Knott, Utah Valley University, CS 2420'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST
from node import TreeNode

class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    Realtional methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    ''' A helper function to build the tree.'''
    with open('around-the-world-in-80-days-3.txt', 'r') as f:
        lines = f.read()
        new_bst = BST()
        for char in lines:
            if char.isalnum():
                new_bst.add(TreeNode(Pair(char)))
        return new_bst

def main():
    ''' Program kicks off here.'''
    test_tree = make_tree()
    test_list = test_tree.inorder()
    print(test_list)
    
if __name__ == "__main__":
    main()
