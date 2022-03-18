
'''

bobcat, cat


'''
def findSubstring(s, target):

    '''
    KMP algo
    TC: O(n)
    SC: O(n)
    - Saves a lot of time from the naive algorithm

    For example if we're given the following....

    s = "aaaxaaax"
    target = "aaaa"

    - Naive algorithm requires you to iterate through each substring of the target size and go through
    the target's element every time...

    - KMP will ensure you never move back when iterating through the string and keep track of the last
    valid character you matched in the target so you can resume from the last valid location instead of
    going from the beginning again

    KMP reduces the redundancies in iterating through the pattern again
    '''
    if not target:
        return 0
    
    # longest prefix suffix at the given index
    lps = [0]*len(target)
    
    # first LPS is always 0 because the LPS can't also be the stirng
    prevLPS, i = 0, 1
    while i < len(target):
        # if we find a matching character, update the LPS
        if target[i] == target[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        else:
            # if there was no long prefix suffix then there's none right now
            if prevLPS == 0:
                lps[i] = 0
                i += 1
            # otherwise, try to find a match
            else:
                prevLPS = lps[prevLPS-1]
    
    i = 0
    j = 0
    while i < len(s):
        if s[i] == target[j]:
            i,j = i+1, j+1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
        if j == len(target):
            return i - len(target)
    return -1

    # '''
    # TC: O(n*t)
    # SC: O(t)
    # '''
    # for i in range(len(s) - len(target) +1):
    #     # O(t)
    #     if s[i:i+len(target)] == target:
    #         return i
    # return -1

print(findSubstring("bobcat", "cat")) #3
print(findSubstring("bob", "cat")) #-1
print(findSubstring("bobca", "cat")) #-1
print(findSubstring("bobcatcat", "cat")) #3