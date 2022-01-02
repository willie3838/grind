'''
Problem Challenge 3
Minimum Window Sort (medium)

Given an array, find the length of the smallest 
subarray in it which when sorted will sort the whole array.

Example 1:
Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Example 2:
Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

Example 3:
Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted

Example 4:
Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.

Approach
- sliding window but check if the sections outside the window are sorted???


TC: O(n)
SC: O(1)
'''

def minimum(nums):
    # find the first non-increasing element
    start = 0
    while start < len(nums)-1 and nums[start] < nums[start+1]:
        start += 1
    
    # find the first non-decreasing elements
    end = len(nums)-1
    while end >= 1 and nums[end] > nums[end-1]:
        end -= 1

    # it's already sorted
    if start > end:
        return 0
    
    # add numbers from outer boundaries on the left
    tmp = nums[start:end+1]
    tmpMin = min(tmp)
    tmpMax = max(tmp)

    while start > 0 and nums[start-1] > tmpMin:
        start -= 1
    
    while end < len(nums)-1 and nums[end+1] < tmpMax:
        end += 1
    
    return end-start+1




print(minimum([1, 3, 7, 2, 5, 4, 6, 10]))
    
        
