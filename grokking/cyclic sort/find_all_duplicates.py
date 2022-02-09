'''
Problem Statement 
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array has some duplicates, find all the duplicate numbers without using any extra space.

Example 1:
Input: [3, 4, 4, 5, 5]
Output: [4, 5]

Example 2:
Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]

[3,4,-4,-5,-5]
'''

def find(arr):
    res = []
    for i in range(len(arr)):
        if arr[abs(arr[i])-1] < 0:
            res.append(abs(arr[i]))
        else:
            arr[abs(arr[i])-1] *= -1
    return res

print(find([3, 4, 4, 5, 5]))