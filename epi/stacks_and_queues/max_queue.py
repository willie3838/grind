from collections import deque
class MaxQueue:
    def __init__(self):
        self.q = deque()
        self.max = deque()

    # monotonic queue concept..
    # takes advantage of the fact that any element that was previously enqueued doesn't matter for the max
    # if it's less than the current elemnt being pushed
    def enqueue(self, val):
        self.q.appendleft(val)
        while self.max and self.max[-1] < val:
            self.max.pop()
        self.max.appendleft(val)
    
    def dequeue(self):
        popped = self.q.pop()
        if popped == self.max[-1]:
            self.max.pop()
        return popped
    
    def max(self):
        return self.max[-1]
    # def __init__(self):
    #     self.q = deque()
    #     self.max = deque()
    
    # # O(1)
    # def enqueue(self, val):
    #     if not max or val >= self.max[-1]:
    #         self.max.append(val)
    #     self.q.appendleft(val)
    
    # # O(1)
    # def dequeue(self):
    #     popped = self.q.pop()
    #     if popped == self.max[-1]:
    #         self.max.pop()
        
    #     return popped
    # # O(n) only when max becomes empty but otherwise O(1)
    # def max(self):
    #     if not self.max:
    #         max.appendleft(max(self.q))
    #     return self.max[0]

'''

enqueue -> 1,5

[5,1]

'''