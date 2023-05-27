
def merge_dicts(dict1, dict2):
    # TODO
    copy1 = dict1.copy()
    copy1.update(dict2)
    return copy1
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
result = merge_dicts(dict1, dict2)
print(result)