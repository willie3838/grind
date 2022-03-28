'''

WEST TO EAST (windows face west)
1,2,3 -> 3,2,1
1,4,3 -> 4,1
1,5,4,3 -> 5,1
1,2,5,2,3 ->5,2,1


3,2,1

sunsets to the west
- have to process from east to west

TC: O(n)
SC: O(n)
'''
def canSeeSunset(buildings):
    res = []

    for i in range(len(buildings)-1,-1,-1):
        while res and buildings[i] >= res[-1]:
            res.pop()
        res.append(buildings[i])
    return res

print(canSeeSunset([1,2,5,2,3]))
print(canSeeSunset([1,2,3]))
print(canSeeSunset([1,1,1]))