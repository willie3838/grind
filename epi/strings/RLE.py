# TC: O(n) SC: O(n)
def encode(s):
    res = ""
    start = 0
    for i in range(1, len(s)):
        if s[start] != s[i]:
            res += str(i - start) + s[start]
            start = i
    
    
    res += str(len(s) - start) + s[start]
    return res 

def decode(s):
    res = ""
    count = 0
    for i in range(len(s)):
        # edge case when the number is > 9
        if s[i].isdigit():
            count = count*10 + int(s[i])
        else:
            res += count*s[i]
            count = 0

    return res

print(encode("eeeeeeeeeeeeeeeeeeeeeeeeffffee"))
print(encode("eeeffffed"))
print(decode(encode("eeeeeeeeeeeeeeeeeeeeeeeeffffee")))