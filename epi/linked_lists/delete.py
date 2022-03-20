
'''

1->2->3->4->5

Neat way of doing O(1) deletion for linked list if the node being deleted isn't the last node
'''
def delete(head, deleteNode):
    deleteNode.val = deleteNode.next.val
    deleteNode.next = deleteNode.next.next
