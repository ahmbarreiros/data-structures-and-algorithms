
def merge_dicts(dict1, dict2):
    # TODO
    merge_dict = dict1.copy()
    for key in dict2:
        if key in merge_dict.keys():
            merge_dict[key] += dict2[key]
        merge_dict.setdefault(key, dict2[key])
    return merge_dict
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
result = merge_dicts(dict1, dict2)
print(result)