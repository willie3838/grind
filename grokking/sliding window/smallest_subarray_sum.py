
'''
Problem Statement 
Given an array of positive numbers and a positive number ‘S’, 
find the length of the smallest contiguous subarray whose sum is 
greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

TC: O(n)
SC: O(1)
'''

def smallest(arr, s):
    start = 0
    summ = 0
    res = float('inf')
    for end,num in enumerate(arr):
        summ += num
        while summ >= s:
            res = min(res, end-start+1)
            summ -= arr[start]
            start += 1
    return res