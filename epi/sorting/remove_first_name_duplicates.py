def removeDuplicates(names):
    names.sort()
    res = []
    for i,(first,last) in enumerate(names):
        if i > 0 and first == names[i-1][0]:
            continue
        res.append((first, last))
    return res

print(removeDuplicates([["Ian", "botham"], ["David", "Gower"], ["Ian", "Bell"],
["Ian", "Chappell"]]))
