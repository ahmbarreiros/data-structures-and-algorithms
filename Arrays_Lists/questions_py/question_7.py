def pair_sum(myList, sum):
    # TODO
    outArr = []
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum:
                outArr.append(f'{myList[i]}+{myList[j]}')
    return outArr
out = pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
print(out)