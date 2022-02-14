'''
Problem Statement 
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
'''

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def reverseList(head, p, q):
    if p == q:
        return head
    
    prevHead = ListNode()
    prevHead.next = head
    pre = prevHead
    
    for i in range(p-1):
        pre = pre.next
    
    curr = pre.next
    prev = None
    
    for i in range(q-p+1):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    pre.next.next = curr
    pre.next = prev


    return prevHead.next

head = Node(1)
curr = head

for i in range(2,4):
    curr.next = Node(i)
    curr = curr.next

res = reverseList(head,1,2)
while res:
    print(res.val)
    res = res.next
