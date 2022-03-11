import string
def encode(col):

    # SC: O(1)
    letters = {}
    counter = 1
    # TC: O(1)
    for char in string.ascii_lowercase:
        letters[char] = counter
        counter += 1

    res = 0
    power = 0
    # TC: O(n)
    for i in reversed(range(len(col))):
        res += letters[col[i].lower()] * (26**power)
        power += 1
    
    return res

    
