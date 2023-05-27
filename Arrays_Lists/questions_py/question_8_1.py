def permutation(list1: list, list2: list):
    if len(list1) != len(list2):
        return False
    
    list1c = list1.copy()
    list2c = list2.copy()
    list1c.sort()
    list2c.sort()
    
    if list1c == list2c:
        return True
    else:
        return False
    
list1 = [1, 2, 5]
list2 = [1, 3, 2]
print(permutation(list1, list2))
    