'''
2^4 = 16
3^2 = 9

if the power is even, we can shift left by y/2 times

2^3 = 8
3^3 = 27

if the power is odd, add the base to it once then continue as
if it was even (any odd number - 1 is even)


3^6 = (3^2)^3 vs 3*3*3*3*3*3*3
3^7 = (3^2)^3 * 3
'''

def pow(x,y):
    res = 1
    
    while y:
        if y&1:
            res *= x
        x = x*x
        y >>= 1
    
    return res


    # # inefficient, take O(y) time which can go up to
    # # 2^31-1
    # while y:
    #     x *= x
    #     y -= 1
    # return x

print(pow(3,6))
print(2 & 1 << 0)