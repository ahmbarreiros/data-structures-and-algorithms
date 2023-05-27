
def count_word_frequency(words):
    # TODO
    dict_words = dict()
    for word in words:
        if word not in dict_words:
            dict_words[word] = 1
        else:
            dict_words[word] += 1
    return dict_words

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
counter = count_word_frequency(words) 
print(counter)