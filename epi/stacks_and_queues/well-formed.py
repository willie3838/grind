
'''

{[]} = True
{[}] = False
{{ = False

TC: O(n)
SC: O(n)
'''
def wellFormed(s):
    stack = []
    for char in s:
        if char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
        elif char == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                return False
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if len(stack) == 0 else False

print(wellFormed("{[]}"))
print(wellFormed("{[}]"))
print(wellFormed("{{"))