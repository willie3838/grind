'''
Case 1: Same length until overlap

1->2
1->2->3->4


Case 2: Different length until overlap 
1->2
3->4->5->2->6

Both should have the same end node...
'''
def isOverlap(l1, l2):

    # TC: O( k )
    while l1 and l2:
        if l1 == l2:
            return True
        l1 = l1.next
        l2 = l2.next
    return False
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
