'''
Problem Challenge 3
Find the First K Missing Positive Numbers (hard)
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Example 1:
Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.

Example 2:
Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.

Example 3:
Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
'''

'''
[1,2,3], k = 2
[-1,-2,-3]

[3,-1,4,5,5], k=3
[3,6,4,6,6]
[3,6,-4,-6,6]

'''

def findFirstK(arr, k):
    i = 0

    # swaps numbers to where they should be
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] > 0 and arr[i] <= len(arr) and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    
    missing = []
    extras = set()

    # adds the missing numbers and keeps track of 
    # numbers that aren't missing
    for i in range(len(arr)):
        if len(missing) < k:
            if arr[i] != i + 1:
                missing.append(i+1)
                extras.add(arr[i])
    
    # adds missing numbers not in the arr/cant be tracked by the indices
    i = 1
    while len(missing) < k:
        candidate = i+len(arr)
        if candidate not in extras:
            missing.append(candidate)
        i += 1
    return missing
    
'''
[5,-1,3,4,5]
'''
print(findFirstK([12,16],2))