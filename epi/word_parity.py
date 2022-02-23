'''
2 = 10
3 = 11
4 = 100
5= 101

12 = 1100
'''
def computeParity(word):

    ones = 0
    while word:
        ones += word & 1
        word >>= 1
    return ones%2
for i in range(1<<16):
    print(i)