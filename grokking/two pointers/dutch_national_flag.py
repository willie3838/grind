
'''
Problem Statement 
Given an array containing 0s, 1s and 2s, sort the array in-place. 
You should treat numbers of the array as objects, 
hence, we can’t count 0s, 1s, and 2s to recreate the array.
The flag of the Netherlands consists of three colors: red, white and blue; 
and since our input array also consists of three different numbers
that is why it is called Dutch National Flag problem.

Example 1:
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

Example 2:
Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]

Approach
- two pointers to keep track of where 0s are and 2s are
- edge case is if we swap a 2 and 0.


2,0,2,1,1,0
0,0,2,1,1,2
0,0,1,1,2,2


TC: O(n)
SC: O(1)
'''

def dutch(nums):
    left = 0
    right = len(nums)-1
    i = 0
    while i <= right:
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
        elif nums[i] == 2:
            nums[right], nums[i] = nums[i], nums[right]
            right -= 1
            i -= 1
        i += 1