# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # def reverse(head):
        #     prev = None
        #     curr = head
        #     while curr:
        #         tmp = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = tmp
        #     return prev

        # l1 = reverse(l1)
        # l2 = reverse(l2)

        sumHead = ListNode(0)
        res = sumHead
        retenue = 0

        while l1 or l2 or retenue:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            retenue = ( res.val + l1_val + l2_val ) // 10
            res.val = ( res.val + l1_val + l2_val ) % 10

            if (l1 and l1.next) or (l2 and l2.next) or retenue:
                res.next = ListNode(retenue)
            else:
                res.next = None

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            res = res.next

        print(sumHead.val)
        # sumHead = reverse(sumHead)

        return sumHead

        

