class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def insert(head, val):
        while head.next:
            head = head.next
        head.next = Node(val)


'''
1->2->2->3->3

TC: O(n)
SC: O(1)
'''
def remove(head):
    curr = head
    while curr:
        distinct = curr.next
        while distinct and distinct.val == curr.val:
            distinct = distinct.next
        curr.next = distinct
        curr = curr.next
    return head





listt = Node(1)
listt.insert(2)
listt.insert(2)
listt.insert(3)
listt.insert(3)

head = remove(listt)

while head:
    print(head.val)
    head = head.next