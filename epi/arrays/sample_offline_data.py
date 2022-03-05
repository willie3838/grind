import random
'''
[1,2,3,4]

'''
def sample(arr, n):
    for i in range(n):
        rdm = random.randrange(0,len(arr))
        arr[i], arr[rdm] = arr[rdm], arr[i]
    return arr[:n]

print(sample([1,2,3,4], 2))