
# TC: O(n) SC: O(1)
def isPalindrome(s):
    start,end = 0, len(s)-1
    while start < end:
        while not s[start].isalnum():
            start += 1
        while not s[end].isalnum():
            end -= 1
        
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True

print(isPalindrome("A man, a plan, a canal, Panama."))
print(isPalindrome("Able was I, ere I saw Elba!"))
print(isPalindrome("Ray a Ray"))
