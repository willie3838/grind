import random

'''
number_of_outcomes = 6
res=0,i=0
res=01,i=1
res=011,i=2
res=0110,i=3

How this works is that we first
find the number of possible outcomes
between a and b.

We then try to randomly generate a number
by forming its bits. The number of bits
is decided by the line while(1 << i) < n
which tries to find 2^i <= number of possible outcomes.

We do this because we can easily generate random numbers between 0 and 2^i-1
where i represents the number of bits (note that 2^i-1 also represents the max number you can form
with i bits)

At the end of the process we'll have a number between 0 and b-a. We just add a to it
to get out result.
'''

'''
res=1,i=1
res=10,i=2
res=100,i=3

k=1*2^i ... n
'''
def generateRandom(a, b):
    n = b-a+1
    while True:
        res = 0
        i = 0
        while (1 << i) < n:
            res = (res << 1) | random.randint(0,1)
            i += 1
        if res <= b:
            break
    return res


    # # Variation 2 (my variation)
    # while True:
    #     res = 0
    #     i = 0
    #     while (1 << i) <= b:
    #         res = (res << 1) | random.randint(0,1)
    #         i += 1
    #     if res <= b:
    #         break
    # return res

print(generateRandom(1,2147483647))