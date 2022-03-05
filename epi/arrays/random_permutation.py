import random
'''

Brute force
- call the rng and add the number to the array
- have a seen set to track what's been used
- if the number has been seen, generate
- repeat until we have an array with same length as the input

TC: O(n log n)
SC: O(n)
'''
def permutation(arr):
    for i in range(len(arr)):
        rdm = random.randrange(i, len(arr))
        arr[i], arr[rdm] = arr[rdm], arr[i]
    
    return arr
    # res = []
    # visited = set()
    # while len(res) < len(arr):
    #     rdm = random.randrange(len(arr))
    #     if rdm not in visited:
    #         visited.add(rdm)
    #         res.append(rdm)

    # return res

print(permutation([0,1,2]))