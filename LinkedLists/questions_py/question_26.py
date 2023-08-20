"""
    Write a function to reverse a singly linked list. The function should return a new linked list that is the reverse of the original list.
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
        
    def reverse(self):
        # TODO
        if(self.length == 0 or self.length == 1): return
        head = self.head
        current_node = self.head.next
        last_node = self.head
        second_last_node = None
        while(last_node is not None):
            last_node.next = second_last_node
            second_last_node = last_node
            last_node = current_node
            if current_node is not None:
                current_node = current_node.next
        self.head = self.tail
        self.tail = head
        
li = LinkedList()
li.append(1)
li.append(2)
# li.append(3)
# li.append(4)
# li.append(5)
print(li)
li.reverse()
print(li)