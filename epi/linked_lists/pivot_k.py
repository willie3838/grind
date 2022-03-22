'''
objective
- pivot a list by k

algorithm
- one list that stores <= k
- one list that stores > k
- connect them
- aiming for o(1) space and o(n) time

'''
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def insert(head, val):
        while head.next:
            head = head.next

        head.next = Node(val)

'''
3,4,2,1,5, k = 2
1,2,3,4,5

Assuming k is within bounds of the list
'''
def pivot(head, k):
    dummyL = currL = Node(-1)
    dummyG = currG = Node(-1)
    dummyE = currE = Node(-1)

    while head:
        if head.val < k:
            currL.next = head
            currL = currL.next
        elif head.val == k:
            currE.next = head
            currE = currE.next
        else:
            currG.next = head
            currG = currG.next
        head = head.next
    currG.next = None
    
    currL.next = currE
    currE.next = dummyG.next
    return dummyL.next

listt = Node(1)
for i in range(2, 6):
    listt.insert(i)

head = pivot(listt, 2)
while head:
    print(head.val)
    head = head.next