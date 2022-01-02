'''
Problem Challenge 1
Quadruple Sum to Target (medium) 
Given an array of unsorted numbers and a target number, 
find all unique quadruplets in it, whose sum is equal to the target number.

Example 1:
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.

Example 2:
Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.

TC: O(n^3)
SC: O(n)
'''

def fourSum(nums, target):
    nums.sort()
    res = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)):
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            start = j + 1
            end = len(nums)-1

            while start < end:
                summ = nums[i] + nums[j] + nums[start] + nums[end]
                if summ == target:
                    res.append([nums[i], nums[j], nums[start], nums[end]])
                    start += 1

                    while start < len(nums) and nums[start] == nums[start-1]:
                        start += 1

                elif summ > target:
                    end -= 1
                else:
                    start += 1
    return res