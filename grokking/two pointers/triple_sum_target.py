'''
Triplet Sum Close to Target (medium)

Problem Statement 
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. 
If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Example 3:
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.

Edge cases
- when we have two cases such that they have the same distance away from the target

TC: O(n^2)
SC: O(1)
'''

def triple(nums, target):
    if len(nums) < 3:
        return 0

    nums.sort()
    res = nums[0]+nums[1]+nums[2]

    # O(n)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        start = i+1
        end = len(nums)-1

        # O(n)
        while start < end:
            summ = nums[start] + nums[end] + nums[i]
            if summ < target:
                start += 1
            elif summ > target:
                end -= 1
            else:
                return summ
            
            if abs(target-summ) < abs(target - res):
                res = summ
            elif abs(target-summ) == abs(target - res):
                res = min(summ, res)
    return res

print(triple([1, 0, 1, 1],100))
