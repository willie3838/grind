class Node:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

'''
1 3 4
2 3 4

'''
def merge(h1, h2): 
    '''
    TC: O(n + m)
    SC: O(1)
    '''   
    dummyHead = Node()
    curr = dummyHead

    while h2 and h1:
        if h2.val < h1.val:
            curr.next = h2
            h2 = h2.next
        else:
            curr.next = h1
            h1 = h1.next
        curr = curr.next

    
    curr.next = h1 or h2
    
    return dummyHead.next

dummy1 = Node()
l1 = Node(1)
dummy1.next = l1

for i in range(1,3):
    l1.next = Node(i+1)
    l1 = l1.next

dummy2 = Node()
l2 = Node(2)
dummy2.next = l2
for i in range(2, 4):
    l2.next = Node(i+1)
    l2 = l2.next


newHead = merge(dummy1.next, dummy2.next)
while newHead:
    print(newHead.val)
    newHead = newHead.next