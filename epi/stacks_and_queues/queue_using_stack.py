class Queue:
    def __init__(self):
        self.enq = self.deq = []

    def enqueue(self, val):
        self.enq.append(val)
    
    def dequeue(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
        if not self.deq:
            raise IndexError("empty queue")
        
        return self.deq.pop()
    
    def peek(self):
        return self.deq[-1] or self.enq[0]



q = Queue()

for i in range(1, 5):
    q.enqueue(i)

'''
[5,4,3,2,1]

'''
print(q.dequeue())
print(q.peek())

print(q.dequeue())
print(q.peek())

print(q.dequeue())
print(q.peek())

