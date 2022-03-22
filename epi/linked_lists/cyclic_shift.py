
'''
1,2,3,4, k=2
3,4,1,2

1,2,3,4, k=3
2,3,4,1

1,2,3,4,5, k=3


- take the last k nodes then shift them to the beginning
'''

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def insert(head, val):
        while head.next:
            head = head.next
        head.next = Node(val)

def shift(head, k):

    length = 0
    curr = head
    while curr:
        curr = curr.next
        length += 1
    
    k = k % length

    if k == 0:
        return head

    fast = head
    for _ in range(k):
        fast = fast.next

    slow = head
    while fast.next:
        slow = slow.next
        fast = fast.next

    prev = slow
    start = slow.next
    tail = slow.next
    while tail.next:
        tail = tail.next
    
    prev.next = None
    tail.next = head
    return start
    


listt = Node(1)
for i in range(2, 6):
    listt.insert(i)

head = shift(listt, 6)
while head:
    print(head.val)
    head = head.next