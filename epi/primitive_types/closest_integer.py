'''
2 = 0010 -> closest is 4 = 0100

5 = 0101 -> closest is 6 = 0110

8 = 1000 -> closest is 4 = 0100

15 = 1111 -> closest is 23 = 1 0111
'''

def sameWeight(x):
    length = 64
    for i in range(length-1):
        if (x << i)&1 != (x<<i+1)&1:
            bit_mask = (1 << i) | (1 << i+1)
            x ^= bit_mask
            return x