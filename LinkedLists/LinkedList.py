class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self) -> str:
        next_node = self.head
        result = ''
        if next_node is not None:
            result += '['
        while next_node is not None:
            result += str(next_node.value)
            if next_node.next is not None:
                result += ', '
            next_node = next_node.next
        if result != '':
            result += ']'
            
        return result
    
    def append(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
    def preprend(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
        
    def insert(self, value, pos):
        if(pos < 1 and pos != -1): return False
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        elif(pos == 1):
            return self.preprend(value)
        elif(pos >= self.length or pos == -1):
            return self.append(value)
        else:
            next_node = self.head
            for i in range(self.length - 1):
                if(i == pos-1):
                    new_node.next = next_node.next
                    next_node.next = new_node
                    break
                next_node = next_node.next
        self.length += 1
        return True
    
    def search(self, target):
        if(self.length == 0): return False
        else:
            next_node = self.head
            for i in range(self.length):
                if next_node.value == target: return True
                next_node = next_node.next
            return False
        
    def get(self, index):
        if(self.length == 0): return -1
        if(index < -1 or index > self.length): return -1
        current_node = self.head
        cont = 0
        while current_node is not None and cont < index:
            cont += 1
            current_node = current_node.next
        if current_node is not None:
            return current_node.value
        else: return -1
    
    

list = LinkedList()
list.append(10)
list.append(5)
list.append(7)
print(list)
print(list)
list.insert(3,2)
print(list)
list.insert(33,-1)
print(list)
print(list.search(5))
print(list.search(400))
print(list.get(4))