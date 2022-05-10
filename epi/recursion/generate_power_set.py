'''

T(n) = T(n-1)*n

TC: O(n*2^n)
SC: O(2^n) <- if we count the output space


        0       1      2
    1      2      2  
 2                
'''
def generatePowerSet(powerSet):
    res = [[]]
    helper(powerSet, [], res)
    return res

def helper(powerSet, path, res):
    for i in range(len(powerSet)):
        res.append(path+[powerSet[i]])
        helper(powerSet[i+1:], path + [powerSet[i]], res)

print(generatePowerSet([0,1,2]))