'''
Problem Statement 
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:
Input: [4, 0, 3, 1]
Output: 2

Example 2:
Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
'''

def findMissing(arr):
    summ = 0
    n = len(arr)

    while n:
        summ += n
        n -= 1

    return summ - sum(arr)

print(findMissing([4,0,3,1]))
print(findMissing([8, 3, 5, 2, 4, 6, 0, 1]))