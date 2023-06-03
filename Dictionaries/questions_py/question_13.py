
def reverse_dict(my_dict):
    # TODO
    return {value: key for key, value in my_dict.items()}
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))