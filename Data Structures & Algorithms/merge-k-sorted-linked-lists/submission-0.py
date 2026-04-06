# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def combine(h1, h2):
    if h2 is None:
        return h1
    
    temp = None
    head = None
    
    while h2 and h1:
        if h1.val > h2.val:
            if temp is None:
                temp = head = h2
                h2 = h2.next
            else:
                temp.next = h2
                temp = temp.next
                h2 = h2.next
        else:
            if temp is None:
                temp = head =h1
                h1 = h1.next
            else:
                temp.next = h1
                temp = temp.next
                h1 = h1.next
    
    if h1 is not None:
        temp.next = h1
    
    if h2 is not None:
        temp.next = h2
    
    return head


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        if len(lists) == 0:
            return None
        else:
            for i in range(len(lists)):
                head_i = lists[i]
                if head is None and head_i:
                    head = head_i
                else:
                    head = combine(head, head_i)
            
        return head
                

        