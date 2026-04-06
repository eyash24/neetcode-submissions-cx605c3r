# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(start, k):
    temp = start
    count = 0
    new_head = new_tail = None
    prev = None

    while count != k and temp:
        prev = temp
        if new_head is None:
            node = ListNode(val=temp.val, next=temp.next)
            new_head = new_tail = node
            temp = temp.next
        else:
            node = ListNode(val=temp.val, next=temp.next)
            node.next = new_head
            new_head = node
            temp = temp.next
        
        count += 1
    
    if count < k:
        return start, prev
    else:
        new_tail.next = temp
        return new_head, new_tail



class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2:
            return head

        new_head = None
        start = head
        tail = None

        while start:
            rev_head, rev_tail = reverse(start, k)
            if new_head is None:
                new_head = rev_head
                tail = rev_tail
                start = tail.next
            
            else:
                tail.next = rev_head
                tail = rev_tail
                start = tail.next

        return new_head

