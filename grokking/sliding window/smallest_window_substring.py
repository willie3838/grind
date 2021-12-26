'''
Problem Challenge 3
Smallest Window containing Substring (hard) 

Given a string and a pattern, 
find the smallest substring in the given string which 
has all the characters of the given pattern.

Example 1:
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:
Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".

Example 3:
Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.

Approach
- sliding window that has a window that goes until it finds the pattern in any substring
- decreases window size once the pattern is found

TC: O(n + k)
SC: O(n + k)
'''

def smallestWindow(s, p):
    if p == "":
        return ""

    freq, window = {},{}

    for char in p:
        freq[char] = freq.get(char, 0) + 1
    
    have, need = 0, len(freq)
    res = (-1,-1)
    resLen = float("inf")
    start = 0

    for end, char in enumerate(s):
        window[char] = window.get(char, 0) + 1

        if char in freq and window[char] == freq[char]:
            have += 1

        while have == need:
            if end-start+1 < resLen:
                res = (start, end)
                resLen = end-start+1

            window[s[start]] -= 1
            if s[start] in freq and window[s[start]] < freq[s[start]]:
                have -= 1
            start += 1
    
    return s[res[0]:res[1] + 1]


print(smallestWindow("aabdec","abc"))
