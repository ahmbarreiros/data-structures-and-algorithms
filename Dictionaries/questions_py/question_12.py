
def max_value_key(my_dict):
    # TODO
    max_value = -1
    max_key = ""
    for key, value in my_dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
    
my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))