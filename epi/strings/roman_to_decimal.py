'''
IV = 4

Usually everything is in decreasing order...

'''

def convert(s):
    mapp = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    res = 0
    for i, char in enumerate(s):

        if char in mapp:
            if i>0 and  mapp[char] > mapp[s[i-1]]:
                res -= mapp[s[i-1]]
                res += mapp[char] - mapp[s[i-1]]
            else:
                res += mapp[char]
    return res

print(convert("LIX")) 

