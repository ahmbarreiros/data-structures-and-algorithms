from numpy import *

arr = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def findNumber(array, number):
    for element in range(len(array)):
        if array[element] == number:
            print(element)
print(findNumber(arr, 8))