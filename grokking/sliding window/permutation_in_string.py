'''
Problem Challenge 1

Permutation in a String (hard) 
Given a string and a pattern, find out if the string contains 
any permutation of the pattern. Permutation is defined as the 
re-arranging of the characters of the string. 
For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba

If a string has ‘n’ distinct characters it will have n!n! permutations.

Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.

Brute force
- create all permutations of "abc" and store in array
- sliding window of size k where k is the length of the pattern

TC: O(n*k! + k!) where n is the length of the string and k is the length of the pattern
SC: O(k!)

Optimized?
- use dictionary to store the frequency of chars
- recheck dictionary at the end of window

TC: O(n*k)
SC: O(k)
'''
def permutationString(s, pattern):
    freq = {}
    for char in pattern:
        freq[char] = freq.get(char, 0) + 1

    start = 0
    for end,char in enumerate(s):
        if char in freq:
            freq[char] -= 1
        if end-start+1 > len(pattern):
            if s[start] in freq:
                freq[s[start]] += 1
            start += 1
        if end-start+1 == len(pattern):
            counter = 0
            for key in freq:
                if freq[key]:
                    counter += 1
            if not counter:
                return True
    return False
'''
BRUTE
def permutationString(s, pattern):
    all = []
    permutations(pattern, [], all)
    start = 0
    for end in range(len(s)):
        if end-start+1 > len(pattern):
            start += 1
        if end-start+1 == len(pattern) and s[start:end+1] in all:
            return True
    return False


def permutations(pattern, path, res):
    if not pattern:
        res.append("".join(path))
        return
    for i,char in enumerate(pattern):
        permutations(pattern[:i] + pattern[i+1:], path+[char], res)'''

print(permutationString("aaacb", "abc"))
