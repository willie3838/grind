'''
Problem Statement 
Given a string, 
find the length of the longest substring which has no repeating characters.

Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".

Approach
- sliding window with a set

Edge cases
baca
bbbb

TC: O(n)
SC: O(n)
'''

def noRepeat(s):
    res = 0
    start = 0
    visited = set()

    for end,char in enumerate(s):
        while char in visited:
            visited.remove(s[start])
            start += 1
        visited.add(char)
        res = max(res, end-start+1)
    return res

print(noRepeat("bbbb"))

