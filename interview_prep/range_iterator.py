class RangeIterator:
    def __init__(self):
        pass

    def range(self, start, end=None, step=1):
        res = []

        if end is None:
            end = start
            start = 0
           
        if step > 0:
            while start < end:
                res.append(start)
                start += step
        else:
            while start > end:
                res.append(start)
                start += step
        return res

arr = [1,2,3]
it = RangeIterator()
print(it.range(len(arr)-1,-1,-1))


