
'''

arr=[1, 2, 3]
p=[0.2, 0.8, 0.1]

rng produces 0.02 -> do we pick 1 or 3???




'''
import bisect
import random
import itertools


def generate(arr, p):
    '''
    TC: O(log n)
    SC: O(n)
    '''
    prob = []
    for i,x in enumerate(p):
        if i == 0:
            prob.append(x)
        else:
            prob.append(x + prob[i-1])
   
    i = bisect.bisect(prob, random.random())
    return arr[i]
    # '''
    # TC: O(n)
    # SC: O(1)
    
    # '''
    # rdm = random.random()
    # prob = 0

    # for i in range(len(p)):
    #     prob += p[i]
    #     if rdm < prob:
    #         return arr[i]
    # return -1

print(generate([1,2,3], [0.2,0.5,0.3]))