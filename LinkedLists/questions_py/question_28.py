"""
    Given a singly linked list, write a function that removes all the duplicates. use this linked list .
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
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def remove_duplicates(self):
        # TODO
        if(self.length == 0 or self.length == 1): return
        aux_arr = []
        current_node = self.head
        last_node = None
        while(current_node is not None):
            if current_node.value not in aux_arr:
                aux_arr.append(current_node.value)
                last_node = current_node
                current_node = current_node.next
            else:
                last_node.next = current_node.next
                current_node = current_node.next
        self.length = len(aux_arr)

li = LinkedList()
li.append(2)
li.append(2)
print(li)
li.remove_duplicates()
print(li)
