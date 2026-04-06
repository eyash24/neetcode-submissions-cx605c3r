# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            prev_ele = None
            current_ele = head

            while current_ele:
               next_ele = current_ele.next
               current_ele.next = prev_ele
               prev_ele = current_ele
               current_ele = next_ele
            

            
            return prev_ele



        else:
            return head