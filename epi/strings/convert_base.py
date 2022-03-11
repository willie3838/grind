'''
convert everything to base 10
then convert back
'''
import math
def convert(number, org, new):
    base10 = 0
    hex = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    counter = 0

    # TC: O(n)
    # converts to base 10
    for i in reversed(range(len(number))):
        if number[i] in hex:
            base10 += hex[number[i]]*org**counter
        else:
            base10 += ((ord(number[i]) - ord('0'))*org**counter)
        counter += 1
    
    # SC: O(n)
    res = ""

    # TC: O(log new)
    # division algorithm
    while base10:
        print(base10 % new, base10, res)
        if base10 % new in hex:
            res += hex[base10 % new]
        else:
            res += chr(base10%new + ord('0'))
        base10 = base10 // new
    
    return res[::-1]
    


print(convert("10",3,16))
# print(int(math.floor(math.log10(2))))
# print(int(math.floor(math.log10(4))))