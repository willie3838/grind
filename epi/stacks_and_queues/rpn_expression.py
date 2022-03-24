'''

12+3x = 9

Need to implement the negative case
'''
def evaluate(tokens):
    digits = []
        
    # O(n)
    for s in tokens:
        
        res = None
        if s == "+":
            res = digits.pop() + digits.pop()
        elif s == "*":
            res = digits.pop() * digits.pop()
        elif s == "-":
            res = -digits.pop() + digits.pop()
        elif s == "/":
            res = int(1/digits.pop() * digits.pop())
        else:
            digits.append(int(s))
        
        if res is not None:
            digits.append(res)
                
    return digits[0]
