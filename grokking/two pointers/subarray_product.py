'''
Problem Statement 

Given an array with positive numbers and a target number, 
find all of its contiguous subarrays whose product is less than the target number.

Example 1:
Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

2,3,2,1


Example 2:
Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.

Approach
- lol it says 2 pointer but i think it's a bit like sliding window

TC: O(n^3)
SC: O(n)
'''

from collections import deque

def subarray(nums, target):
    currProduct = 1
    start = 0
    res = []

    # O(n)
    for end, num in enumerate(nums):
        currProduct *= num
        
        # O(1)
        while currProduct >= target:
            currProduct /= nums[start]
            start += 1
        
        tmp = deque()
        # O(n)
        '''
        pretty cool how this prevents duplicates by reversing how the input gets put into the deque
        '''
        for i in range(end, start-1, -1):
            tmp.appendleft(nums[i])
            res.append(list(tmp))
    return res

print(subarray([2,5,3,10], 30))

