'''

Problem Statement 
Given the head of a Singly LinkedList, reverse the LinkedList.
Write a function to return the new head of the reversed LinkedList.

1 -> 2 -> 3
3 -> 2 -> 1
'''

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def listReverse(head):
    curr = head
    prev = None

    while curr:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt

    return prev

head = Node(1)
curr = head

for i in range(2,4):
    curr.next = Node(i)
    curr = curr.next


# while head:
#     print(head.val)
#     head = head.next

res = listReverse(head)
while res:
    print(res.val)
    res = res.next
