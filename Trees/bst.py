'''Hunter Knott, Utah Valley University, CS 2420'''
from node import TreeNode

class BST:
    '''A BST ADT that stores individual characters read from a file'''
    def __init__(self, tree_size = 0):
        self.root = None
        self.tree_size = tree_size
        self.tree_values = []

    def is_empty(self):
        '''Returns True if the tree is empty'''
        if self.root is None:
            return True
        return False

    def size(self):
        '''Returns the size of the tree'''
        return self.tree_size

    def height(self):
        '''Returns the height of the tree'''
        if self.root is None:
            return 0
        return max(self.height_helper(self.root.left), self.height_helper(self.root.right)) + 1
    
    def height_helper(self, trav_root):
        '''Helper function to recursively find the height of left and right subtrees'''
        if trav_root is None:
            return 0
        left_height = self.height_helper(trav_root.left)
        right_height = self.height_helper(trav_root.right)
        return max(left_height, right_height) + 1

    def add(self, item):
        '''Adds an item to its proper place in the tree'''
        if self.root is None:
            self.root = item
            self.tree_size += 1
        else:
            cursor = self.root
            while cursor:
                if item.data.letter < cursor.data.letter:
                    if cursor.left is None:
                        cursor.left = item
                        cursor = None
                        self.tree_size += 1
                    else:
                        cursor = cursor.left
                elif item.data.letter > cursor.data.letter:
                    if cursor.right is None:
                        cursor.right = item
                        cursor = None
                        self.tree_size += 1
                    else:
                        cursor = cursor.right
                elif item.data.letter == cursor.data.letter:
                    cursor.data.count += 1
                    cursor = None
        return self

    def remove(self, item):
        '''Removes a given item in the tree'''
        self.remove_helper(self.root, item)
        return self

    def remove_helper(self, trav_root, item):
        '''Helper function to recursively remove a node'''
        if trav_root is None:
            return None
        if trav_root.data.letter > item.letter:
            trav_root.left = self.remove_helper(trav_root.left, item)
        elif trav_root.data.letter < item.letter:
            trav_root.right = self.remove_helper(trav_root.right, item)
        else:
            if trav_root.right is None:
                return trav_root.left
            if trav_root.left is None:
                return trav_root.right
            temp_node = trav_root.right
            while temp_node.left:
                temp_node = temp_node.left
            trav_root.right = self.remove_helper(trav_root.right, trav_root.data)
        return trav_root

    def find(self, item):
        '''Returns the item that is searched'''
        cursor = self.root
        while cursor is not None:
            if item.letter == cursor.letter:
                return cursor
            elif item.letter < cursor.letter:
                cursor = cursor.left
            else:
                cursor = cursor.right
        raise ValueError("The given value is not in the tree")

    def inorder(self):
        '''Performs an inorder traversal, and returns a list of values'''
        if self.root:
            self.tree_values = []
            cursor = self.root
            self.inorder_helper(cursor)
            return self.tree_values

    def inorder_helper(self, trav_root):
        '''Helper function to recursively perform an inorder traversal'''
        if trav_root:
            self.inorder_helper(trav_root.left)
            self.tree_values.append(trav_root.data)
            self.inorder_helper(trav_root.right)

    def preorder(self):
        '''Performs a preorder search, and returns a list of values'''
        if self.root:
            self.tree_values = []
            cursor = self.root
            self.preorder_helper(cursor)
            return self.tree_values

    def preorder_helper(self, trav_root):
        '''Helper function to recursively perform a preorder traversal'''
        if trav_root:
            self.tree_values.append(trav_root.data)
            self.preorder_helper(trav_root.left)
            self.preorder_helper(trav_root.right)

    def postorder(self):
        '''Performs a postorder search, and returns a list of values'''
        if self.root:
            self.tree_values = []
            cursor = self.root
            self.postorder_helper(cursor)
            return self.tree_values

    def postorder_helper(self, trav_root):
        '''Helper function to recursively perform a postorder traversal'''
        if trav_root:
            self.postorder_helper(trav_root.left)
            self.postorder_helper(trav_root.right)
            self.tree_values.append(trav_root.data)

    def rebalance(self):
        '''Puts all tree items in the correct order'''
        self.value_list = self.inorder()
        self.root = None
        self.add(TreeNode(self.rebalance_helper(self.value_list)))
        return self

    def rebalance_helper(self, sublist):
        '''Helper function to recursively rebalance the tree'''
        if len(sublist) == 0:
            return None
        if len(sublist) == 1:
            return sublist[0]
        mid_value = sublist[len(sublist) // 2]
        first_half = sublist[:len(sublist) // 2]
        second_half = sublist[(len(sublist) // 2) + 1:]
        self.rebalance_helper(first_half)
        self.rebalance_helper(second_half)
        return mid_value