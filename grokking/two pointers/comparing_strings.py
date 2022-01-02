'''
Problem Challenge 2
Comparing Strings containing Backspaces (medium)

Given two strings containing backspaces (identified by the character ‘#’), 
check if the two strings are equal.

Example 1:
Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

Example 2:
Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.

Example 3:
Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.

Example 4:
Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.

Approach
- stack to store the characters, pop when we see # then compare the stacks afterwards

Edge cases
- start with backspaces 

TC: O(n+m)
SC: O(n+m)
'''

def comparing(s1, s2):
    i = 0
    j = 0

    stack1 = []
    stack2 = []


    while i < len(s1):
        if stack1 and s1[i] == '#':
            stack1.pop()
        elif s1[i] != '#':
            stack1.append(s1[i])
        i += 1

    while j < len(s2):
        if stack2 and s2[j] == '#':
            stack2.pop()
        elif s2[j] != '#':
            stack2.append(s2[j])
        j += 1
    print(stack1, stack2)

    return stack1 == stack2

print(comparing("xy#z", "xzz#"))