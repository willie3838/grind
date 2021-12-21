'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, 
find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].


Edge cases
k > len(arr)
arr empty
k = 0

TC: O(n)
SC: O(1)
'''

def maximumSum(arr, k):
    start = 0
    res = 0
    summ = 0
    for end, num in enumerate(arr):
        summ += num
        if end-start+1 > k:
            summ -= arr[start]
            start += 1
        res = max(summ, res)
    return res

print(maximumSum([2, 3, 4, 1, 5],0))