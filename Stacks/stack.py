'''Hunter Knott, Utah Valley University, CS 2420'''
from node import StackNode

class Stack:
    '''A stack ADT that stores mathematical expressions'''
    def __init__(self):
        self.highest = None
        self.cursor = None
        self.stack_size = 0
        self.precedence = {'+': 1, '-': 1, '*': 2, '/':2}

    def push(self, item):
        '''Places a new item at the top of the stack'''
        new_node = StackNode(item)
        if self.highest:
            new_node.below = self.highest
        self.highest = new_node
        self.stack_size += 1

    def pop(self):
        '''Removes and returns top stack value'''
        if self.highest is None:
            raise IndexError("There are no elements on the stack")
        pop_value = self.highest.value
        self.highest = self.highest.below
        self.stack_size -= 1
        return pop_value

    def top(self):
        '''Returns the top element value on the stack'''
        if self.highest is None:
            raise IndexError("There are no elements on the stack")
        return self.highest.value

    def size(self):
        '''Returns the number of elements on the stack'''
        return self.stack_size

    def clear(self):
        '''Removes all elements from the stack'''
        self.highest = None
        self.cursor = None
        self.stack_size = 0

    def __str__(self):
        output = ""
        for node in self:
            output += str(node.value) + "\n"
        return output

    def __iter__(self):
        self.cursor = self.highest
        return self

    def __next__(self):
        if self.cursor is None:
            raise StopIteration
        temp = self.cursor
        self.cursor = self.cursor.below
        return temp
