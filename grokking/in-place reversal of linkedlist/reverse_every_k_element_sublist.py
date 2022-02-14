'''

Problem Statement 
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.
If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

'''

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def reverse(head, k):
    dummy = ListNode()
    dummy.next = head
    
    length = 0
    curr = head
    
    while curr:
        curr = curr.next
        length += 1
    
    length = length // k
    preHead = dummy
    curr = preHead.next
    

    for i in range(length):
        prev = None
        for i in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        tmp = preHead.next
        preHead.next.next = curr
        preHead.next = prev
        preHead = tmp
        
    return dummy.next