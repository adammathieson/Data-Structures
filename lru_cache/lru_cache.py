import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = {}



    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_front(key)
            return node
        else:
            None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #See if it's in the dict
        if key in self.storage:
            self.storage[key] = value
            # self.storage[key].value = value
            self.order.move_to_front(key)
        elif self.size == self.limit:
            print("Tail+++++>", self.order.tail.value)
            print("Head+++++>", self.order.head.value)
            key_to_delete = self.order.remove_from_tail()
            self.storage.pop(key_to_delete)
            self.storage[key] = value
            self.order.add_to_head(key)
        else:
            self.storage[key] = value
            self.order.add_to_head(key)
            if self.size < self.limit:
                self.size += 1

            
# test = {}
# test['a'] = 1
# test['b'] = 2
# # test['a'] = 2

# test.pop('a')

# print(DoublyLinkedList())

# print(test)

# test = LRUCache()

# test.set("a", 10)
# test.set("b", 1)
# test.set("c", 1)

# print(test.get("a"))
# print(test.order.tail.value)
