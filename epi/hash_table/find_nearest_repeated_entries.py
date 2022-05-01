from sklearn.utils import resample


def findClosestPair(words):
    mapp = {}
    res = float('inf')

    for i,word in enumerate(words):
        if word in mapp:
            res = min(res, i - mapp[word])
        mapp[word] = i
    return res
