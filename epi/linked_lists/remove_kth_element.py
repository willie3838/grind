'''

1->2->3->4, 1  = 1->2->3

1->2->3->4, 2  = 1->2->4

One way is to find the length of the list...
Go to the length-kth element and set its next pointer to None then return the head
But apparently we can't store the length...

'''
def remove_kth(head, k):
    if not head:
        return None
    fast = head
    for _ in range(k):
        fast = fast.next

    slow = head
    prev = None
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next
    
    
    prev.next = slow.next
    return head
