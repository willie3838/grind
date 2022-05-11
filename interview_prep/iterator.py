class Iterator:
    def __init__(self, arr):
        self.arr = arr
        self.i = 0

    def next(self):
        if self.i >= len(self.arr):
            return None
        res = self.arr[self.i]
        self.i += 1
        return res
    
    def hasNext(self):
        return True if self.i < len(self.arr) else False



arr = [1,2,3]
it = Iterator(arr)

for _ in range(4):
    print(it.next())
    print(it.hasNext())