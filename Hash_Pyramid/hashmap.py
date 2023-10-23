'''Hunter Knott, Utah Valley University, CS 2420'''
from item import TableItem

class HashMap:
    '''A HashMap ADT that stores key-value pairs'''
    def __init__(self, init_capacity = 7):
        self.init_capacity = init_capacity
        self.curr_capacity = init_capacity
        self.table = [None] * init_capacity

    def hash_key(self, key):
        '''Hashing function that returns a bucket value from a given key'''
        key_string = str(key[0]) + str(key[1])
        return int(key_string) % self.curr_capacity

    def get(self, key):
        '''Searches for a given key and returns its value'''
        bucket_index = self.hash_key(key) % len(self.table)
        item = self.table[bucket_index]
        while item is not None:
            if key == item.key:
                return item.value
            item = item.next
        raise KeyError("The given key has no item")

    def set(self, key, value):
        '''Inserts a given key-value pair into the table'''
        bucket_index = self.hash_key(key) % len(self.table)
        item = self.table[bucket_index]
        previous = None
        while  item is not None:
            if key == item.key:
                item.value = value
                return True
            previous = item
            item = item.next
        if self.table[bucket_index] is None:
            self.table[bucket_index] = TableItem(key, value)
        else:
            previous.next = TableItem(key, value)
        if (self.size() / self.capacity()) >= 0.8:
            self.resize()
        return True

    def remove(self, key):
        '''Removes a given key-value pair from the table'''
        bucket_index = self.hash_key(key) % len(self.table)
        item = self.table[bucket_index]
        previous = None
        while item is not None:
            if key == item.key:
                if previous is None:
                    self.table[bucket_index] = item.next
                else:
                    previous.next = item.next
                return True
            previous = item
            item = item.next
        return False

    def clear(self):
        '''Removes all items from the table'''
        self.curr_capacity = self.init_capacity
        self.table = [None] * self.init_capacity

    def capacity(self):
        '''Returns current table capacity'''
        return self.curr_capacity

    def size(self):
        '''Returns current number of items in the table'''
        table_size = 0
        for element in self.table:
            if element is not None:
                table_size += 1
        return table_size

    def resize(self):
        '''Increases table capacity, and rehashes all elements'''
        temp_list = []
        for element in self.table:
            if element is not None:
                temp_list.append(element)
        self.curr_capacity = (self.curr_capacity * 2) - 1
        self.table = [None] * self.curr_capacity
        for element in temp_list:
            self.set(element.key, element.value)

    def keys(self):
        '''Returns a list of all keys in the table'''
        key_list = []
        for element in self.table:
            if element is not None:
                key_list.append(element.key)
        return key_list
