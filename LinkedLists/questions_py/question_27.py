"""
    Write a function to find and return the middle node of a singly linked list. If the list has an even number of nodes, return the second of the two middle nodes.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def find_middle(self):
        # TODO
        if self.length == 0: return None
        isEven = self.length % 2 == 0
        current_node = self.head
        for _ in range(self.length // 2):
            current_node = current_node.next
        return current_node

li = LinkedList()
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)
print(li.find_middle().value)
