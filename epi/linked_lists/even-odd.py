'''
Objective
- even numbered nodes comes first then odd numbered

algorithm
- counter to check if we're at an even or odd numbered node
- two pointers to lists that only store even numbered and odd numbered nodes
- combine them
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

1,2,3,4 -> 1,3,2,4
1,2,3,4,5 -> 1,3,5,2,4
'''
def merge(head):
    dummyEven = currEven = Node(-1)
    dummyOdd = currOdd = Node(-1)
    counter = 0

    while head:
        if counter % 2 == 0:
            currEven.next = head
            currEven = currEven.next
        else:
            currOdd.next = head
            currOdd = currOdd.next
        counter += 1
        head = head.next
    
    currEven.next = dummyOdd.next
    currOdd.next = None
    return dummyEven.next


listt = Node(1)
for i in range(2, 6):
    listt.insert(i)

head = merge(listt)
while head:
    print(head.val)
    head = head.next