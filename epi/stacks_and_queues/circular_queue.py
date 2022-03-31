from collections import deque

class CircularQueue:
    def __init__(self, capacity):
        self.q = deque()
        self.capacity = capacity

    
    def enqueue(self, val):
        self.q.appendleft(val)
        self.capacity += 1
    
    def dequeue(self):
        self.capacity -= 1
        return self.q.pop()

    def size(self):
        return self.capacity