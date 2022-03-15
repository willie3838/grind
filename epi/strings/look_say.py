
from re import I

# TC: O(n * k) where n is the input and k is the length of the string generated in between
# SC: O(k) 
def lookSay(n):
    res = "1"
    
    # O(n)
    while n-1:
        curr = ""
        i = 0
        # O(k) not O(k^2)
        while i < len(res):
            tmp = i
            # O(k)
            while i < len(res) and res[i] == res[tmp]:
                i += 1
           
            curr += chr(i - tmp + ord('0'))
            curr += res[i-1]
        res = curr
        n -= 1
    return res


print(lookSay(6))
