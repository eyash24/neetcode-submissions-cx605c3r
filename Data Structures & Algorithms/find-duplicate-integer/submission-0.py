class ListNode:
    def __init__(self, val: ListNode = None, next: ListNode = None):
        self.val = val
        self.next = next

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        head = None
        curr = None

        for n in nums:
            new_node = ListNode(val=n)
            if head is None:
                head =curr= new_node
            else:
                temp = head
                while temp:
                    if temp.val == n:
                        return n
                    temp = temp.next
                
                curr.next = new_node
                curr = curr.next





        