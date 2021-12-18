'''
Problem Statement 
Given an array containing 0s and 1s, 
if you are allowed to replace no more than ‘k’ 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.

Example 1:
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Example 2:
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

Approach
- find the longest window of 1s with k 0s


Edge cases
- cant think of any that would break this code??
- what if all were 1s??

TC: O(n)
SC: O(1)

'''

def longestOnes(arr, k):
    start = 0
    zeros = 0
    res = 0

    for end, val in enumerate(arr):
        if val == 0:
            zeros += 1

        while zeros > k:
            if arr[start] == 0:
                zeros -= 1
            start += 1

        res = max(end - start + 1, res)
    
    return res

print(longestOnes([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(longestOnes([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))