'''
Problem Statement 
Given a sorted array, create a new array 
containing squares of all the number of the 
input array in the sorted order.

Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]


-2,-1,0,2,3
[0,1.4,4,9]

Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]

Edge cases
[1,2,3,4]
[-3,-2,-1] -> [1,4,9]

Approach
- start from the end and compare to the beginning
- if the beginning > end, swap them and square the new end, update the end

TC: O(n)
SC: O(1)
'''

def square(arr):
    res = [0]*len(arr)
    left = 0
    right = len(arr)-1
    i = len(arr)-1

    while left <= right:
        if arr[left]**2 > arr[right]**2:
            
            res[i] = arr[left]**2
            left += 1
        else:
            res[i] = arr[right]**2
            right -= 1
        i -= 1


    return res

