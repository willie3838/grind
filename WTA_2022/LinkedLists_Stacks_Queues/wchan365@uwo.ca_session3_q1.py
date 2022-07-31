
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

import heapq
'''

Uses a min heap to store all the nodes in ascending order

'''
def mergeKLists(arr, k):
    minHeap = []
    for node in arr:
        curr  = node
        while curr:
            heapq.heappush(minHeap, curr.val)
            curr = curr.next
    
    dummy = Node(-1)
    curr = dummy
    while minHeap:
        curr.next = Node(heapq.heappop(minHeap))
        curr = curr.next
    
    return dummy.next

def createList(node, values):
    curr = node
    idx = 0
    while idx < len(values):
        curr.next = Node(values[idx])
        idx += 1
        curr = curr.next
    return node

def printNode(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    print(arr)

def tests():
    # Given test cases
    l1 = createList(Node(1), [5,7])
    l2 = createList(Node(2), [3,6,9])
    l3 = createList(Node(4), [8,10])
    arr = [l1, l2, l3]
    # Expected: 1->2->3-4>-5>6->7->8->9->10
    res = mergeKLists(arr, 3)
    printNode(res)

    # My test cases
    l1 = None
    l2 = createList(Node(2), [3,6,9])
    l3 = createList(Node(4), [8,10])
    arr = [l1, l2, l3]
    # Expected: 2->3-4->6->8->9->10
    res = mergeKLists(arr, 2)
    printNode(res)

    arr = []
    # Expected: 2->3-4->6->8->9->10
    res = mergeKLists(arr, 0)
    printNode(res)


if __name__ == "__main__":
    tests()






