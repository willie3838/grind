

def applyPermute(arr, perm):

    for i in range(len(perm)):
        end = perm[i]

        while end != i:
            # if the current cycle has already been traversed...
            if end < i:
                break
            end = perm[end]
        else:
            # only start making the permutation once we've found a cycle
            completeCycle(i, arr, perm)
    
    return arr

    # # save space but downgrade TC
    # def cyclic(start, perm, arr):
    #     i, temp = start, arr[start]
    #     while True:
    #         next_i = perm[i]
    #         next_temp = arr[next_i]
    #         arr[next_i] = temp
    #         i, temp = next_i, next_temp
    #         if i == start:
    #             break
        
    # for i in range(len(arr)):
    #     j = perm[i]
    #     while j != i:
    #         if j < i:
    #             break
    #         j = perm[j]
    #     else:
    #         cyclic(i, perm, arr)
    # return arr


    res = [0]*len(arr)
    for i,num in enumerate(perm):
        res[num] = arr[i]
    return res


def completeCycle(start, arr, perm):
    curr_i = start
    curr_el = arr[start]

    while True:

        next_i = perm[curr_i]
        next_el = arr[next_i]

        arr[next_i] = curr_el

        curr_el = next_el
        curr_i = next_i

        if curr_i == start:
            break 
    
'''
["d","b","a","c","e"]


'''
print(applyPermute(["a","b","c","d","e"], [2,4,3,0,1]))