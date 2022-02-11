'''
Problem Challenge 1
Find the Corrupt Pair (easy)
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
 The array originally contained all the numbers from 1 to ‘n’, but due to a data error, 
 one of the numbers got duplicated which also resulted in one number going missing. 
 Find both these numbers.

Example 1:
Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.

Example 2:
Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
'''
def findCorrupt(arr):
    res = []
    for i in range(len(arr)):
        value = abs(arr[i])-1
        if arr[value] < 0:
            res.append(value+1)
        else:
            arr[value] *= -1
    
    for i,num in enumerate(arr):
        if num > 0:
            res.append(i+1)
            return res
    return res

print(findCorrupt([3, 1, 2, 5, 2]))
print(findCorrupt([3, 1, 2, 3, 6, 4]))