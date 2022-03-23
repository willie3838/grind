'''
3,1,4 = 413
709 = 907
0231 = 1320

- traverse through both lists
- o()
'''

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def insert(head, val):
        while head.next:
            head = head.next
        head.next = Node(val)

'''
3,1,4 = 413
7,0,9 = 907
0,2,3,1 = 1320


9,9,9
1

0 0 0 1
'''
def add(l1, l2):
    dummy = curr = Node(-1)
    carry = 0

    # TC: O(n + m) SC: O( max(m, n) )
    while l1 or l2 or carry:
        summ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

        if summ < 10:
            carry = 0
        else:
            carry = 1
        
        curr.next = Node(summ % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

l1 = Node(9)
l1.insert(9)
l1.insert(9)

l2 = Node(1)


head = add(l1, l2)

while head:
    print(head.val)
    head = head.next
