# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l3 = head = None
        carry = 0
        l1_none = False
        l2_none = False

        while l1 or l2:
            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val
            
            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val
            
            add_val = l1_val + l2_val + carry
            # print('add_val: ', add_val)

            if add_val > 9:
                carry = 1
                add_val = add_val - 10
            else:
                carry = 0

            new_node = ListNode(val=add_val)
            # print('new_node.val: ', new_node.val)

            if l3 is None:
                l3 = head = new_node
            else:
                # print('Inserting')
                l3.next = new_node
                l3 = l3.next
            
            if l1 is not None:
                l1 = l1.next
            
            if l2 is not None:
                l2 = l2.next
        
        if carry == 1:
            new_node = ListNode(val=1)
            l3.next = new_node

        return head

            

        