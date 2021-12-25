'''
Problem Challenge 2
String Anagrams (hard) 

Given a string and a pattern, find all anagrams of the pattern 
in the given string. Anagram is actually a Permutation of a string. 
For example, “abc” has the following six anagrams:
abc
acb
bac
bca
cab
cba

Write a function to return a list of starting indices 
of the anagrams of the pattern in the given string.

Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

- dictionary to store the frequency of chars
- sliding window of size k where k is the length of the pattern
- if we find a match, store the start index in the result


TC: O(n*k)
SC: O(k)

'''

def anagrams(s, pattern):
    freq = {}
    for char in pattern:
        freq[char] = freq.get(char, 0)+1
    start = 0
    res = []
    
    for end, char in enumerate(s):
        if char in freq:
            freq[char] -= 1
        
        if end-start+1 > len(pattern):
            if s[start] in freq:
                freq[s[start]] += 1
            start += 1
        
        if end-start+1 == len(pattern):
            print(freq, end, start)
            counter = 0
            for key in freq:
                if freq[key] != 0:
                    counter += 1
            if counter == 0:
                res.append(start)
            if s[start] in freq:
                freq[s[start]] += 1
            start += 1
    
    return res

print(anagrams("ppqp", "pq"))