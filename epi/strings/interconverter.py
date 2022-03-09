import math

def convert(input):
    if type(input) == str:
        return stringToInt(input)
    else:
        return intToString(input)
        

# TC: O(n) SC: O(1)
def intToString(input):
    res = ""
    if input < 0:
        input *= -1
        res += "-"

    while input:
        digits = int(math.log10(input))+1
        res += chr(input // 10**(digits-1) + 48)
        input %= 10**(digits-1)
    return res

    

# TC: O(n) SC: O(1)
def stringToInt(input):
    negative = False
    if input[0] == "-":
        negative = True
    res = 0
    for i in range(1, len(input)):
        res = res*10 + (ord(input[i])-48)
      
    return res if not negative else res*-1

print(convert("-123"))
print(convert(-123))