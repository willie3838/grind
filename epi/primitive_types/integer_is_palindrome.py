import math
from re import L

'''
Given 234, return False

'''
def isPalindrome(x):

    # primitive operations
    n = int(math.floor(math.log10(x))+1)
    print(n)
    for i in range(n):
        lsb = x%10
        msb = x // 10**(n-2*i-1)

        if lsb != msb:
            return False
        x = x - (msb * 10**(n-2*i-1))
        x = x//10
        
    return True

    # # brute force O(n)
    # x = str(x)
    # start, end = 0, len(x)-1

    # while start < end:
    #     if x[start] != x[end]:
    #         return False
    # return True

print(isPalindrome(1234321))