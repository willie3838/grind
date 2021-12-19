
   
'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Approach
- use a dictionary to store freq of each character
- sliding window

Edge cases
aababccccccccce <- checking to see if window resizing actually works

TC: O(n)
SC: O(k) <- only stores k characters at most
'''

def longestk(str, k):
    start = 0
    freq = {}
    res = 0

    for end, char in enumerate(str):
        freq[char] = freq.get(char, 0) + 1

        if len(freq) > k:
            freq[str[start]] -= 1
            if freq[str[start]] == 0:
                freq.pop(str[start])
            start += 1
        res = max(res, end-start+1)
    
    return res

print(longestk("araaci", 2))