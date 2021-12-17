'''

Problem Statement 
Given an array of characters where each character represents a fruit tree, 
you are given two baskets and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, i.e., 
you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.

Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']


Approach
- Find a window where we have the longest sequence of letters that only contain 2 distinct letters


EDGE CASES
Input: Fruit=['A','C','A','B','C','B','B','C']
Input: Fruit=['A','B','C']
Input: Fruit=['A']

TC: O(n)
SC: O(1) <- at most we'll have 2 

'''

def totalFruit(self, fruits: List[int]) -> int:
    start = 0
    res = 0
    visited = {}

    if not fruits:
        return res


    for end in range(len(fruits)):
        visited[fruits[end]] = visited.get(fruits[end], 0) + 1
        if len(visited) > 2:
            visited[fruits[start]] -= 1
            if visited[fruits[start]] == 0:
                visited.pop(fruits[start])
            start += 1
        res = max(res, end-start+1)
    return res
