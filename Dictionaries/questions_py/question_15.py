
def check_same_frequency(list1, list2):
    # TODO
    new_dict = dict()
    for item in list1:
        new_dict[item] = new_dict.get(item, 0) + 1
    print(new_dict)
    for item in list2:
        if item in new_dict.keys():
            return False
    return True
    
    # for item in list1:
    #     if item in list2:
    #         return False
    # return True
    
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
result = check_same_frequency(list1, list2)
print(result)