'''
[1,2,3] -> [1,3,2]
[1,2,3,4] -> [1,3,2,4]
[1,2,3,4,5] -> [1,3,2,5,4]

- sort the array first

while...
- swap the third element from the current element with the second
- go to the third element
- repeat until end of array


what if the array isn't sorted...

[1,4,5,1,3] -> [1,4,2,5,3]
'''


'''
    Proof by contradiction:

    Assuming that the algorithm doesn't produce an alternating array...

    Suppose that there's an odd index i such that A[i] >= A[i+1] in the array. 
    This is impossible because in line 38 and 39, we make sure that A[i] will be < A[i+1]


    Can usually prove by contradiction to show a f
 
'''

def makeAlternate(arr):

    # O(n) optimal
    # need to realize that we can take a greedy approach -> every element in an odd index needs 
    # to be greater than everything around it
    # we can prove this is correct by showing that with each iteration the number of swaps reduces
    # or that as we go through the array, everything before it will be in the correct state
    for i in range(len(arr)-1):
        if i%2:
            arr[i], arr[i+1] = (arr[i+1], arr[i]) if arr[i] < arr[i+1] else (arr[i], arr[i+1])
        else:
            arr[i], arr[i+1] = (arr[i], arr[i+1]) if arr[i] < arr[i+1] else (arr[i+1], arr[i])
    return arr


   
   

    # # O(n log n)
    #  if len(arr) < 3:
    #   return arr
    # arr.sort()
    # i = 2

    # # O(n)
    # while i < len(arr):
    #     arr[i], arr[i-1] = arr[i-1], arr[i]
    #     i += 2
    
    # return arr

print(makeAlternate([1,2,3]))
print(makeAlternate([1,2,3,4]))
print(makeAlternate([1,2,3,4,5]))
print(makeAlternate([1,4,5,2,3]))