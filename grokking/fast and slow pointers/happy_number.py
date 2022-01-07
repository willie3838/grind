'''
Problem Statement 
Any number will be called a happy number if, 
after repeatedly replacing it with a number equal to 
the sum of the square of all of its digits, 
leads us to number ‘1’. All other (not-happy) 
numbers will never reach ‘1’. 
Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

'''

def isHappy(self, n: int) -> bool:
    slow = n
    fast = self.getNext(n)
    
    while slow != fast:
        slow = self.getNext(slow)
        fast = self.getNext(self.getNext(fast))
    return fast == 1
    
    
    def getNext(self, n):
        summ = 0
        while n > 0:
            summ += (n%10)**2
            n //= 10
            
        return summ
