'''
x = 1
1,2

'''
import math
def square_root(x):
    l,r = (1.0,x) if x >= 1.0 else (x,1.0)

    while not math.isclose(l, r):
        mid = 0.5 * (l + r)
        if mid*mid > x:
            r = mid
        else:
            l = mid
    return l


print(square_root(4))

