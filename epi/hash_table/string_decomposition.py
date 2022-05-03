'''


foobarthemebarfoo     foo,bar

TC: O(nk)
'''
def computeStringDecomposition(sentence, words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    wordLen = len(words[0])
    length = len(words)
    res = []

    # O(n - k) where n is the length of the sentence
    for i in range((len(sentence)-wordLen*length)+1):
        seen = {}
        # O(k) where k is the number of words
        for j in range(length):
            word = sentence[i+j*wordLen : i+j*wordLen + wordLen]
            if word in freq:
                seen[word] = seen.get(word, 0) + 1
            
            if seen[word] > freq[word]:
                break

            if j + 1 == length:
                res.append(i)
    return res
