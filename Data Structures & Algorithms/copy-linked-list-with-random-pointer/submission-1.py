"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None

        dict_ll = dict()
        curr = head
        curr_copy = None
        head_copy = None

        # 1st pass -> create the nodes
        while curr:
            key = str(curr.val) + str(curr.random) + str(curr.next)
            dict_ll[key] = Node(x=curr.val)
            curr = curr.next
        
        # 2nd pass -> add pointers to next and random
        curr = head
        while curr:
            key = str(curr.val) + str(curr.random) + str(curr.next)

            if head_copy is None and curr_copy is None:
                head_copy = curr_copy = dict_ll[key]
            
            if curr.next is None:
                curr_copy.next = None
            else:
                key_next = str(curr.next.val) + str(curr.next.random) + str(curr.next.next)
                curr_copy.next = dict_ll[key_next]

            if curr.random is None:
                curr_copy.random = None
            else:
                key_random = str(curr.random.val) + str(curr.random.random) + str(curr.random.next)
                curr_copy.random = dict_ll[key_random]
            
            curr_copy = curr_copy.next
            curr = curr.next

        return head_copy

        