'''
Problem Challenge 1
Palindrome LinkedList (medium)
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.
Example 1:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false

TC: O(n)
SC: O(1)
'''

def isPalindrome(self, head: Optional[ListNode]) -> bool:     
    # find middle
    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # reverse middle
    curr = slow.next
    slow.next = None
    tmp = None
    
    while curr:
        nxt = curr.next
        curr.next = tmp
        tmp = curr
        curr = nxt
    
    
    # check the 2 halves
    head1 = tmp
    head2 = head
    
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next

    
    return True
            