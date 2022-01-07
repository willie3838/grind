'''
TC: O(n)
SC: O(1)
'''
def hasCycle(self, head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False
    slow = head
    fast = head.next

    while fast and fast.next and slow != fast:
        slow = slow.next
        fast = fast.next.next
    return slow == fast