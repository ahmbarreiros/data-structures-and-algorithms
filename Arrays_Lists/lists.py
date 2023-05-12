#   Created by Elshad Karimov on 10/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Accessing/Traversing the list

shoppingList = ['Milk', 'Cheese', 'Butter']

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    # print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")


# Update/Insert - List 

myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15)

myList.append(55)

newList = [11,12,13,14]
myList.extend(newList)
print(myList)


#  Searching for an element in the List
myList =  [10,20,30,40,50,60,70,80,90]

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchinList(myList, 100))


#  List operations / functions
total = 0 
count = 0
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1 
    average = total / count
					
print('Average:', average)



numlist = list() 
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
					
average = sum(numlist) / len(numlist) 
print('Average:', average)

## List comprehension
prev_list = [1, 2, 3]
new_list = []
for i in prev_list:
    multiply_2 = i * 2
    new_list.append(multiply_2)
print('before')
print(new_list)

# new_list = [new_item for item in list]
new_list = [i * 2 for i in prev_list]
print("after")
print(new_list)

language = "Python"
new_list = [letter for letter in language]
print(new_list)

# Conditional list comprehension
prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
# new_list = [new_item for item in list if condition]
new_list = [number for number in prev_list if number > 0]
print(new_list)

prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
new_list = [number**2 for number in prev_list if number < 0]
print(new_list)

sentence = "My name is Elshad"
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

# other method
def get_number(number):
    return number if number > 0 else "negative number"

prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
new_list = [get_number(number) for number in prev_list] # nesse caso é necessário usar o else
print(new_list)