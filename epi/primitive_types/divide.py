'''
2/2 = 1

0010
0010

0001


4/2 = 2

0100
0010

0010

How this works is that we find the highest integer
that can divide the dividend and we repeat this

Another version is to use the fact there are 32 bits
and find the largest (2^k)*y that can divide x
'''


def divide(x, y):
    res = 0
    # because we have 32 bits
    power = 32
    y_power = y << power

    # while loop until we've fully divided x
    while x >= y:
        # find the highest (2^k)*y that divides into x
        while y_power > x:
            y_power >>= 1
            power -= 1
        
        # add 2^k to the result
        res += 1 << power
        # update x
        x -= y_power
    return res

    # res = 0
    # while x >= y:
    #     tmp = y
    #     mul = 1
    #     while x >= tmp:
    #         x -= tmp
    #         res += mul
    #         mul += mul
    #         tmp += tmp
            
    # return res

    # res = 0
    # while x:
    #     x -= y
    #     res += 1
    # return res

print(divide(27,3))