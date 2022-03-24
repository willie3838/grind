'''
- Not the exact q, but gonna advance it further...
'''

class Node:
    def __init__(self, val, next=None,  prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self, head=None):
        self.head = head
        self.tail = head


    def insert(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.max = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    # assuming that the node is in the linked list..
    def remove(self, node):
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
        elif self.head:
            node.prev.next = node.next
            node.next.prev = node.prev


import heapq
from collections import defaultdict
class MaxStack:    
    def __init__(self):
        self.stack = DLL()
        self.mapp = defaultdict(list)
        # use this to track the max
        self.temp = []
        
    def push(self, val):
        if not self.temp or val >= self.temp[-1]:
            self.temp.append(val)

        node = Node(val)
        self.stack.insert(node)
        self.mapp[val].append(node)

    def pop(self):
        key = self.stack.tail.val
        node = self.stack.tail

        if key == self.temp[-1]:
            self.temp.pop()

        if len(self.mapp[key]) == 1:
            self.mapp.pop(key)
        else:
            self.mapp[key].remove(node)
        
        self.stack.remove(node)
        return node

    def peek(self):
        return self.stack.tail.val
        
    
    def max(self):
        return self.temp[-1]
    
    def popMax(self):
        maxx = self.temp.pop()
        node = self.mapp[maxx][-1]
        if len(self.mapp[maxx]) == 1:
            self.mapp.pop(maxx)
        else:
            self.mapp[maxx].pop()
        self.stack.remove(node)
        return node



stack = MaxStack()
stack.push(10)
stack.push(5)
stack.push(100)
print(stack.max())
stack.popMax()
print(stack.max())
stack.popMax()
print(stack.max())