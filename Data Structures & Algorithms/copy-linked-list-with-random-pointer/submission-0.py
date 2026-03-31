"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        # Linked list traversal

        copy_head = Node(head.val)

        oldToCopy = {
            None: None,
        }
        oldToCopy[head] = copy_head

        curr = head
        copy_curr = copy_head

        while curr.next:
            curr = curr.next
            copy_curr.next = Node(curr.val)
            copy_curr = copy_curr.next
            oldToCopy[curr] = copy_curr

        # Traversal following the random pointers
        curr = head
        copy_curr = copy_head
        
        while curr:
            copy_curr.random = oldToCopy[curr.random]
            curr = curr.next
            copy_curr = copy_curr.next

        return copy_head




