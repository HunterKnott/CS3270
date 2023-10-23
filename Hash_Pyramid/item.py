'''Hunter Knott, Utah Valley University, CS 2420'''

class TableItem:
    '''Items that can be added or removed from a Hash Table'''
    def __init__(self, itemKey, itemValue):
        self.key = itemKey
        self.value = itemValue
        self.next = None