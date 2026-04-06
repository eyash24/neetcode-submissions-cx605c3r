# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val >= list2.val:
                current_ele = list2
                head = current_ele
                list2 = list2.next
            else:                
                current_ele = list1
                head = current_ele
                list1 = list1.next
        elif list1 and not list2:
            return list1
        else:
            return list2


        while list1 and list2:
            if list1.val >= list2.val:
                current_ele.next = list2
                current_ele = current_ele.next
                list2 = list2.next
            else:
                current_ele.next = list1
                current_ele = current_ele.next
                list1 = list1.next
        
        if list1:
            current_ele.next = list1
            return head
        
        if list2:
            current_ele.next = list2
            return head