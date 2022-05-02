def findSubarray(arr, keywords):
    mapp = {}
    for word in keywords:
        mapp[word] = 1
    
    start = 0
    foundStart = False
    end = 0

    for i, sentence in enumerate(arr):
        for word in sentence:
            if word in mapp:
                start = i if not foundStart else start
                end = i
                break
    
    return arr[start:end+1]

