'''
Problem Statement 
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

TC: 

'''

def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    fast = head
    slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
        if fast == slow:
            break
    
    if not fast or not fast.next:
        return None
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow