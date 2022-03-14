

def reverseWords(s):
    # non-pythonic way would be to iterate from the back and append it to a list
    return " ".join(s.split()[::-1])

print(reverseWords("Alice likes Bob"))   