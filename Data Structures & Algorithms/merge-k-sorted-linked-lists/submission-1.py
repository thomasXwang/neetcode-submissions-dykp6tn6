# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy


        while len(lists) > 0:
            possible_nodes = [head for head in lists if head]
            min_node = min([head.val for head in possible_nodes])
            min_index = [head.val for head in possible_nodes].index(min_node)

            tail.next = lists[min_index]
            tail = tail.next
            if lists[min_index].next:
                lists[min_index] = lists[min_index].next
            else:
                lists.remove(lists[min_index])

        return dummy.next

