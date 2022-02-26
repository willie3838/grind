'''
badWords = jerk* *lame*

{
    j: { e: {r: {k: {*: {#:#}}}}}
}


'''




def censor(badWords, message):
    trie = {}

    for word in badWords.split():
        curr = trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr["#"] = "#"

    curr = trie
    i = 0
    res = list(message)

    while i < len(message):
        start = i
        while i < len(message) and message[i] != " ":
            i += 1
        if isBad(message[start:i], trie):
            for j in range(start, i):
                if res[j].isalpha():
                    res[j] = "*"
        i += 1

    return "".join(res)

def isBad(word, trie):
    if not word and "#" in trie:
        return True
    if not word and "#" not in trie:
        return False

    bad = False
    if not word[0].isalpha():
        bad = bad or isBad(word[1:], trie)
    else:
        if word[0] in trie:
            bad = bad or isBad(word[1:], trie[word[0]])
        if "*" in trie:
            bad = bad or isBad(word[1:], trie) or isBad(word[1:], trie["*"])
    return bad
    
print(censor("jerk", "(jerk)"))
print(censor("lame *lame", "llame"))
print(censor(badWords="lame *lame", message="llllame"))
print(censor(badWords="lame lard", message="he's a dawdlame lardadawd"))
print(censor(badWords="lame jerk", message="he's a lamebird jerk"))
print(censor(badWords="lame jerk", message="he's a lamebird jerkawd"))
print(censor(badWords="lame jerk", message="he's a lamebird dawdjerk"))
print(censor(badWords="lame* jerk", message="he's a lamebird jerk"))
print(censor(badWords="*lame* jerk", message="he's a (adlamebird jerk"))

    # '''
    # Cases

    # Ends
    # - At punctuation and at the end of a bad word
    # - At punctuation and at the en dof a bad word with wild card at end
    # - At punctuation and end of regular word
    
    # Going through
    # - Current char not in bad word but bad word has wild card at the beginning
    # - Current char not in bad word
    # - Current char in bad word


    # TRY DOING A RECURSIVE APPROACH WITH BACKTRACKING
    # '''
    # for i,char in enumerate(message):
    #     if char in punctuation:
    #         # end of bad word with wild card at end or at the end of bad word without wildcard
    #         if "*" in curr and "#" in curr["*"] or char in punctuation and "#" in curr:
    #             res += "*"*(i-start) + char
    #         # reached end of the word but not a bad word
    #         elif "#" not in curr:
    #             res += message[start:i+1]
    #         start = i+1
    #         curr = trie
    #     else:
    #         # if there's a wildcard and the current character is part of the bad word, exit out of 
    #         # wild card
    #         if "*" in curr and char in curr["*"]:
    #             curr = curr["*"]
    #             curr = curr[char]
    #         # if the character is part of a bad word and it's at the beginning of the word
    #         # then we go to the next character
    #         elif char in curr and (curr != trie or message[i-1] in punctuation):
    #             curr = curr[char]
    #         # if there's a wildcard at the start and the character isn't part of the bad word
    #         # then we stay on the wildcard
    #         elif "*" in curr and char not in curr["*"]:
    #             continue
    #         else:
    #             curr = trie
           
    # print(curr)
    # if curr != trie and "#" in curr:
    #     res += "*"*(len(message)-start)
    # else:
    #     res += message[start:]
    # return res






