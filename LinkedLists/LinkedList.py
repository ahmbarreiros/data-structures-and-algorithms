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
        
    def insert(self, value, index):
        if(index < 1 and index != -1): return False
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        elif(index == 0):
            return self.preprend(value)
        elif(index >= self.length or index == -1):
            return self.append(value)
        else:
            next_node = self.head
            for i in range(self.length):
                if(i == index):
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
            return current_node
        else: return -1
        
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if(self.length == 0): return None
        popped_node = self.head
        if(self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0: return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            past_node = None
            
            while current_node.next is not None:
                past_node = current_node
                current_node = current_node.next
            self.tail = past_node
            self.tail.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if self.length == 0: return None
        if index < 0 and index != -1 or index > self.length: return None
        if index == -1 or index == self.length - 1:
            return self.pop()
        elif index == 0:
            return self.pop_first()
        else:
            current_node = self.head
            if self.length == 1:
                self.head = self.tail = None
            else:
                past_node = None
                for _ in range(index):
                    past_node = current_node
                    current_node = current_node.next
                past_node.next = current_node.next
                current_node.next = None
        self.length -= 1
        return current_node
    
    def delete_all(self):
        self.head = self.tail = None
        self.length = 0
    

list = LinkedList()
list.append(10)
list.append(5)
list.insert(3, 2)
list.insert(4, 0)
list.insert(33, -1)
# list.delete_all()
print(list)