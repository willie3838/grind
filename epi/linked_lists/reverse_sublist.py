class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def insert(head, val):
        while head.next:
            head = head.next
        head.next = Node(val)

'''

1->2->3->4, 2,4

making the assumption that start and end are always in bounds

1->2->3->4 1,4 (full reverse case)
1->2->3->4 1,3 (partial front reverse)


1->2->3->4 2,4 (parital back reverse)

TC: O( end )
SC: O(1)
'''
def reverse(head, start, end):
    dummy = Node(-1)
    dummy.next = head

    curr = head
    prevHead = dummy
    for _ in range(start-1):
        prevHead = curr
        curr = curr.next
    
    prev = None
    for _ in range(end - start + 1):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    prevHead.next.next = curr
    prevHead.next = prev

    return dummy.next


listt = Node(1)
listt.insert(2)
listt.insert(3)
listt.insert(4)

head = reverse(listt, 1, 1)

while head:
    print(head.val)
    head = head.next