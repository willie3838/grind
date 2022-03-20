'''

1 -> 3 -> 4
     6 <- 5
TC: O(F+C) where F is the number of nodes and C is the length of the cycle
'''

def isCyclic(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if not fast or not fast.next:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow
