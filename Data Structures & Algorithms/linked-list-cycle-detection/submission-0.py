# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        setll = set()
        index = 0
        if head:
            while head:
                if head not in setll and head.next not in setll:
                    print(head)
                    setll.add(head)
                    head = head.next
                else:
                    return True
        else:
            return False

        return False