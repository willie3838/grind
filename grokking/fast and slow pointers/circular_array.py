'''
Problem Challenge 3
Cycle in a Circular Array (hard)
We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. 
Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:
If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.
Example 1:
Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
Example 2:
Input: [2, 2, -1, 2]
Output: true
Explanation: The array has a cycle among indices: 1 -> 3 -> 1
Example 3:
Input: [2, 1, -1, -2]
Output: false
Explanation: The array does not have any cycle.

TC: O(n)
SC: O(1)
'''
# def circularArrayLoop(self, nums: List[int]) -> bool:
#         for i,num in enumerate(nums):
#             mark = str(i)
#             while type(nums[i]) == int and num * nums[i] > 0 and nums[i] % len(nums) != 0:
#                 jump = nums[i]
#                 nums[i] = mark
#                 i = (i + jump)%len(nums)
            
#             if nums[i] == mark:
#                 return True
#         return False


def mergeSort(nums):

    if len(nums) == 1:
        return nums

    start = 0
    end = len(nums)
    mid = (start+end)//2

    left = mergeSort(nums[start:mid])
    right = mergeSort(nums[mid:end])
    

    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0

    res = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    while i < len(left):
        res.append(left[i])
        i += 1
    
    while j < len(right):
        res.append(right[j])
        j += 1
    
    return res


print(mergeSort([5,4,3,2,1]))