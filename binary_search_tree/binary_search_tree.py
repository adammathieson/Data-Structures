import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            #go left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            #go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        if target < self.value:
            # go left
            if not self.left:
                # It's not here
                return False
            else:
                return self.left.contains(target)
        else:
            # go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Recursive solution
        # if not self.right:
        #     return self.value
        # return self.right.get_max()

        # Iterative Solution
        max_value = self.value
        current = self

        while current:
            # if current value is greater than max we update it
            if current.value > max_value:
                max_value = current.value

            current = current.right

        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Recursive Solution
        # cb(self.value)

        # if self.left:
        #     self.left.for_each(cb)
        # if self.right:
        #     self.right.for_each(cb)

        #Iterative
        stack = []
        stack.append(self)

        while len(stack):
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # values = []
        # if a node is passed in recursion, else it ends
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        storage = Queue()
        storage.enqueue(self)

        while storage.len() > 0:
            current = storage.dequeue()
            print(current.value)
            if current.left:
                storage.enqueue(current.left)
            if current.right:
                storage.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        storage = Stack()
        storage.push(self)

        while storage.len() > 0:
            current = storage.pop()
            print(current.value)
            if current.left:
                storage.push(current.left)
            if current.right:
                storage.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

#Reverse linked list solution - not tested
    # def reverse(listHead):
    # prev = None
    #     current = listHead
    #     next = listHead.next

    #     while current:
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next

    #     listhead = prev


# test = []
# test.append(1)
# test.append(2)
# test.append(3)

# print('test:', test)