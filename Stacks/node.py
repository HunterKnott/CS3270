'''Hunter Knott, Utah Valley University, CS 2420'''

class StackNode:
    '''Nodes that can be pushed or popped from the stack'''
    def __init__(self, val):
        self.value = val
        self.below = None
    
    def __str__(self):
        return f'{self.value}'