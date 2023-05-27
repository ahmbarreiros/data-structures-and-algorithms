def contains_duplicate(nums):
    # TODO
    nums_set = set()
    for element in nums:
        if element not in nums_set:
            nums_set.add(element)
        else:
            return True
nums = [1,2,3,1]
result = contains_duplicate(nums)
print(result)