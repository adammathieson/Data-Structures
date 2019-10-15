import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        item = self.storage.remove_from_head()
        self.size -= 1
        return item
    

    def len(self):
        return self.size


queue = Queue()
queue.enqueue(1)
queue.enqueue('test')

print(queue.len())
print(queue.dequeue())
