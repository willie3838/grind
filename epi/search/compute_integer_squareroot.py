
'''
n = 4

0,1,2,3,4


n = 16

0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
'''

def find(n):
    l,r = 0,n
    res = -1
    while l <= r:
        mid = (l+r)//2
        
        if mid**2 <= n:
            res = max(res, mid)
            l = mid + 1
        else:
            r = mid - 1
    return res

print(find(78))
