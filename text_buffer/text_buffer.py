import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Text_buffer:
    def __init__(self, init=None):
        self.storage = DoublyLinkedList()

        if init:
            self.append(init)

    def __str__(self):
        # Print the contents of buffer
        s = ""
        current = self.storage.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, str_to_add):
        for char in str_to_add:
            self.storage.add_to_tail(char)

    def prepend(self, str_to_add):
        for char in str_to_add[::-1]:
            self.storage.add_to_head(char)

    def delete_front(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.storage.remove_from_head()

    def delete_back(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.storage.remove_from_tail()

    def join(self, other_buffer):
        
        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storage.head.prev = self.storage.tail
        other_buffer.storage.head = self.storage.head
        self.storage.tail = other_buffer.storage.tail

    def split(self, split_point):
        pass

    def join_string(self, string_to_join):
        # new_buffer = Text_buffer(string_to_join)
        # self.join(new_buffer) 
        # or

        self.append(string_to_join)

if __name__ == '__main__':
    text = Text_buffer("Super")

    print(text)

    text.join_string("califragilisticexpealidocious")

    print(text)

    text.append(" is ")
    text.join(Text_buffer("weird."))

    print(text)

    text.delete_back(6)
    print(text)

    text.prepend("Hey! ")
    print(text)

    text.delete_front(5)
    print(text)