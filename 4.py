'''4) 	Given an array of integers, your task is to find the maximum sum of a contiguous subarray. A contiguous subarray is defined by selecting a range of elements from the array without skipping any element.
 Write a function that takes a list of integers nums as input and returns the maximum sum of a contiguous subarray. [-2, 1, -3, 4, -1, 2, 1, -5, 4], output: 6 -> [4, -1, 2, 1]'''

def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums)) # Output=6