def sum_of_pairs(arr, n):
    for i in range(len(arr) // 2):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == n:
                print([arr[i], arr[j]])
sum_of_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
# sum_of_pairs([2, 3, 6, 9], 9)

# best solution
def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
 
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")