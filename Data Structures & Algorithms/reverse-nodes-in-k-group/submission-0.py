# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Step 1: check if there are at least k nodes left in the list
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head

        # Step 2: Reverse the first k nodes
        prev = None
        curr = head
        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # Step 3
        head.next = self.reverseKGroup(curr, k)

        return prev