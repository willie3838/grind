'''
2 * 2 

0010
0010

0100

2 * 3

0010
0011

0110


'''


'''
3x4 = 12

0011
0100

x=0011,y=0100,rs=0
x=0001,y=1000,rs=0100
x=0000,y=0000,rs=1100

5x3 = 15

0101
0011

x=0101,y=0011,rs=0
x=0010,y=0110,rs=0011
x=0001,y=1100,rs=1111

2x1 = 1
2x2 = 2
2x3 = 6

All integers can be represented with base 2... So we can break it down further and multiply
the integer by bits instead of the whole number. This is sort of like how we do long multiplication
and multiply by the digits first then add everything up

Basically how this works is that we add (2^k)*y to the result every time x's kth bit is 1.
'''
def multiply(x, y):
    running_sum = 0
    while x:
        if x&1:
            running_sum = add(running_sum, y)
        x,y = x >> 1, y << 1
    return running_sum

def add(a, b):
    running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a ,b
    while temp_a or temp_b:
        ak, bk = a&k, b&k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        running_sum |= ak ^ bk ^ carryin
        carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
    return running_sum | carryin
