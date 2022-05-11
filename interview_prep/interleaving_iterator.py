'''
[1,2]
[1,2,3,4]

Try the O(1) implementation
'''
import collections

class InterleavingIterator:
    def __init__(self, arr1, arr2):
        self.queue = collections.deque()
        i,j = 0, 0

        while i < len(arr1) or j < len(arr2):
            if i < len(arr1):
                self.queue.append(arr1[i])
                i += 1
            if j < len(arr2):
                self.queue.append(arr2[j])
                j += 1

    def next(self):
        return self.queue.popleft()
    
    def hasNext(self):
        return True if self.queue else False

arr1 = [1,2]
arr2 = [1,2,3,4]   
it = InterleavingIterator(arr1, arr2)


for _ in range(6):
    print(it.next())