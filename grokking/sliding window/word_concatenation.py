'''
Problem Challenge 4

Words Concatenation (hard) 
Given a string and a list of words, 
find all the starting indices of substrings in the given string 
that are a concatenation of all the given words exactly once without any overlapping of words. 
It is given that all words are of the same length.

Example 1:
Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Example 2:
Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".

Approach
- window must be size of len(words[0])*len(words)
- any time we're at end%len(words[0]) == 0, we check if it's in words
- if it's in words, we add the word into a visited set
- if it's already in visited set, we decrease the window size
- if len(set) == len(words), we add start to our res


TC: O(n*k)
SC: O(k)
'''

def concatenate(s, w):
    if len(w) == 0 or len(w[0]) == 0:
        return []

    freq = {}
    for word in w:
        freq.get(word, 0) + 1
    
    res = []
    wordCount = len(w)
    wordLength = len(w[0])

    for i in range((len(s) - wordCount * wordLength)+1):
        seen = {}
        for j in range(wordCount):
            nextWordIndex = i + j * wordLength
            word = s[nextWordIndex: nextWordIndex + wordLength]

            if word not in freq:
                break

            if word not in seen:
                seen[word] = seen.get(word, 0) + 1
            
            if seen[word] > freq[word]:
                break

            if j+1 == wordCount:
                res.append(i)
    return res

print(concatenate("catdogfoxdogcat", ["cat","fox"]))
