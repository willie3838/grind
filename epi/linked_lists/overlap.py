'''
Case 1: Same length until overlap

1->2
1->2->3->4


Case 2: Different length until overlap 
1->2
3->4->5->2->6

Both should have the same end node...
'''
def isOverlap(headA, headB):

    if not headA or not headB:
        return None

    lengthA = getLength(headA)
    lengthB = getLength(headB)

    if lengthA < 0:
        return findCycle(headA)
    
    if lengthB < 0:
        return findCycle(headB)

    if lengthB < lengthA:
        headA, headB = headB, headA
        lengthA, lengthB = lengthB, lengthA

    diff = lengthB - lengthA

    for _ in range(diff):
        headB = headB.next

    while headB and headA and headB != headA:
        headB = headB.next
        headA = headA.next

    if headB != headA:
        return None

    return headB


# assume that there is always a cycle
def findCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    
    return fast
    
    
# returns -1 if there's a cycle
def getLength(head):
    length = 0
    if hasCycle(head):
        return -1
    
    while head:
        head = head.next
        length += 1
    
    return length
    

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if fast == slow:
        return True
    else:
        return False

    # # TC: O( k ) actually wont work if one list is shorter than the other and we reach the end before we can match...
    # while l1 and l2:
    #     if l1 == l2:
    #         return True
    #     l1 = l1.next
    #     l2 = l2.next
    # return False

    # '''
    # TC: O(n + m)
    # SC: O(1)

    # Maybe reduce TC to O(max(n, m))
    
    # '''
    # if not l1 or not l2:
    #     return False

    # while l1.next:
    #     l1 = l1.next

    # while l2.next:
    #     l2 = l2.next
    
    # return l1 == l2
