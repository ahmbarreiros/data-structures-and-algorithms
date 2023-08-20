"""
    Write a function to delete a node from a singly linked list. The function should take the index(starting from 0) of the node to be deleted as a parameter.
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
        
    def remove(self, index):
        if(index < 0 or index >= self.length): return None
        remove_node = self.head
        if(self.length == 0): return None
        elif(index == 0): 
            if(self.length == 1):
                self.head = self.tail = None
            else:
                self.head = self.head.next
            remove_node.next = None
        else:
            last = remove_node
            i = 0
            while(remove_node is not None and i < index):
                last = remove_node
                remove_node = remove_node.next
                i += 1
            if(remove_node is not None):
                if(remove_node.next is None):
                    self.tail = last
                    last.next = None
                else:
                    last.next = remove_node.next
                remove_node.next = None
            else:
                return None
        self.length -= 1
        return remove_node
        
li = LinkedList()
li.append(10)
li.append(30)
li.append(20)
print(li)
li.remove(0)
print(li)