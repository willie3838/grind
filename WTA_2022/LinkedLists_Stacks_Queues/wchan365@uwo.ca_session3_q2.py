
from regex import R


def removeMinBrackets(s):
    left = 0
    tmp = ""

    # removes any unbalanced RIGHT brackets
    for char in s:
        if char == ")" and left == 0:
            continue
        elif char == "(":
            left += 1
        elif char == ")":
            left -= 1
            
        tmp += char
    
    res = ""
    # removes any unbalanced LEFT brackets
    for char in tmp[::-1]:
        if char == "(" and left != 0:
            left -= 1
            continue
        res += char
        
            
    return res[::-1]
        

def tests():
    # Given test cases
    s = "a)b(c)d"
    # Expected output ab(c)d
    print(removeMinBrackets(s))

    # My test cases
    s = "a(b(c("
    # Expected otuput abc
    print(removeMinBrackets(s))

    s = "a(b(c()"
    # Expected otuput a(bc)
    print(removeMinBrackets(s))


if __name__ == "__main__":
    tests()
