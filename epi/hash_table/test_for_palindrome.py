'''
abba

a:2
b:2

abbba

aaabaaa
TC: O(n)
SC: O(n)

- Stores the frequency of each char
- If the char frequency is divisible by 2 then that means it can be mirrored in a palindrome
- The only time it can't be divisible by 2 is if there's an odd length, but
this can only happen once...
'''
def canBePalindrome(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    bad = 0
    for char in freq:
        if freq[char] % 2 != 0:
            bad += 1
    
    return True if bad <= 1 else False

print(canBePalindrome("abbba"))