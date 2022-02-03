def ordered_pairs(arr):
    freq = {}
    res = 0
    for i,num in enumerate(arr):
        res += 1
        diff = arr[i] - i

        if diff in freq:
            res += freq[diff]*2
        freq[diff] = freq.get(diff, 0) + 1
    return res

'''
(1,1)*2, (2,2)*2, (3,3)*2

(1,2),(2,1)
(3,2),(2,3)
(1,3),(3,1)

'''

print(ordered_pairs([1,2,3]))
        
