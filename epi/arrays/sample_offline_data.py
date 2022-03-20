import random
'''
Uses the fishers yates shuffle. The reason why this is uniformly random....

Imagine you have 3 balls in a hat and you want to construct
a random permutation of them:

probability ball is 1st: 1/n
probability ball is 2nd: n-1/n * 1/n-1 = 1/n 
probability ball is 3rd: n-1/n * n-2/n-1 *1/n-2 = 1/n

This is essentially what the algorithm is doing
'''
def sample(arr, n):
    for i in range(n-1, 0, -1):
        rdm = random.randrange(0,i+1)
        arr[i], arr[rdm] = arr[rdm], arr[i]
    return arr[:n]

print(sample([1,2,3,4], 2))