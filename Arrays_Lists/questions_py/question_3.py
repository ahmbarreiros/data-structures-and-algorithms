def middle(lst):
    middle = lst[:]
    del middle[0], middle[-1]
    return middle