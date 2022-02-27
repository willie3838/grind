'''

[1,1,1] -> True
[1,0,1] -> False
[2,0,0] -> True

[3,3,3,3]
'''

'''
                       3
            33        333          3333
         333  3333    3333
        3333

  length of tree = 2
  number of leaf nodes = 2
  tc = 4

'''
def canAdvance(arr):
    maxx, last_index = 0, len(arr)-1
    i = 0

    '''
    finds the max place we can go to at each location
    we can only enter a location if it's within our max
    '''
    while i <= maxx and maxx < last_index: 
        maxx = max(maxx, arr[i]+i)
        i += 1
    return maxx >= last_index
    # if len(arr) == 1:
    #     return True
    # maxSteps = arr[0]
    # res = False
    # for i in range(1, maxSteps+1):
    #     res = res or canAdvance(arr[0+i:])
    
    # return res

# print(canAdvance([1,1,1]))
# print(canAdvance([1,0,1]))
# print(canAdvance([2,0,0]))
print(canAdvance([3,2,0,0,2,0,1]))