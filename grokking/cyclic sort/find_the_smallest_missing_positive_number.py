'''
Problem Challenge 2

Find the Smallest Missing Positive Number (medium)
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:
Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'

Example 2:
Input: [3, -2, 0, 1, 2]
Output: 4

Example 3:
Input: [3, 2, 5, 1]
Output: 4

[2,1,0]
[-2,-1,0]

'''

def findSmallest(arr):
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[i] = len(arr)+1
    
    for i in range(len(arr)):
        value = abs(arr[i])
        if value <= len(arr) and arr[value-1] > 0:
            arr[value-1] *= -1

    for i in range(len(arr)):
        if arr[i] > 0:
            return i + 1
    return len(arr)+1
        
'''
[-1,-1,0,-1,2]
'''
print(findSmallest([1,1]))

