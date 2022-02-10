'''

Problem Statement 
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example 1:
Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

Example 2:
Input: [2, 4, 1, 2]
Output: 3

Example 3:
Input: [2, 3, 2, 1]
Output: 4
'''

def findAllMissing(arr):
    for i in range(len(arr)):
        value = abs(arr[i])-1
        if arr[value] > 0:
            arr[value] *= -1
    
    res = []
    for i in range(len(arr)):
        if arr[i] > 0:
            res.append(i+1)
    return res

print(findAllMissing([2, 3, 1, 8, 2, 3, 5, 1]))
print(findAllMissing([2, 4, 1, 2]))
print(findAllMissing([2, 3, 2, 1]))