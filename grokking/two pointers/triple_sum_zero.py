'''
Problem Statement 
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

TC: O(n^2)
SC: O(n)
'''

def triple_zero(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        # prevents duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue

        start = i + 1
        end = len(nums) - 1

        while start < end:
            summ = nums[i] + nums[start] + nums[end]
            if summ == 0:
                res.append([nums[i], nums[start], nums[end]])

                # prevents duplciates
                tmp = nums[start]
                while start < len(nums) and tmp == nums[start]:
                    start += 1
            elif summ > 0:
                end -= 1
            else:
                start += 1
    return res