'''
Problem Challenge 2
Rotate a LinkedList (medium)

Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
'''

def rotate(head, k):
    if not head:
        return head
    length = 0
    curr = head
    while curr:
        curr = curr.next
        length += 1
    
    if k % length == 0:
        return head
    
    length = k % length
    fast = head
    
    while length:
        fast = fast.next
        length -= 1
    
    slow = head
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    newHead = slow.next
    fast.next = head
    slow.next = None
    
    return newHead