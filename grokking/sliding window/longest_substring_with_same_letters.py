'''
Problem Statement 
Given a string with lowercase letters only, 
if you are allowed to replace no more than ‘k’ letters with any letter, 
find the length of the longest substring having the same letters after replacement.

Example 1:
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".


Approach
- sliding window
- use a dictionary to store the most frequent chars in the window
- if the most frequent chars - length of windows > k, we need to readjust window


Edge
"ababccbb", k=2
"abaccc", k=2



 String="aabccbb", k=2
'''

def longestSubstring(str, k):
    start = 0
    freq = {}
    res = 0

    for end, char in enumerate(str):
        freq[char] = freq.get(char, 0) + 1
        max_freq = max(freq.values())

        if end - start + 1 - max_freq > k:
            freq[str[start]] -= 1
            if freq[str[start]] == 0:
                freq.pop(str[start])
            start +=1 
        res = max(res, end - start + 1)
    return res


