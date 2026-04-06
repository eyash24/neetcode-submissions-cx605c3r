class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        present = None
        prev = None
        print(f'n: {n}')

        while curr:
            print(f'\ncurr.val: {curr.val}, curr.next:{curr.next}')
            count += 1
            if count > n:
                if prev is None:
                    prev = head
                else:
                    prev = prev.next
                print(f'prev.val:{prev.val}, prev.next:{prev.next}')
            
            if count >= n:
                if present is None:
                    present = head
                else:
                    present = present.next
                print(f'present.val:{present.val}, present.next:{present.next}')

            curr = curr.next

        # present is the element to be deleted 
        # present.next is the element after the deleted element
        # prev is the element before the deleted element
        if present == head:
            return present.next
        if present and prev is None and present.next is None:
            return None
        elif present and prev is not None and present.next is None:
            prev.next = None
        elif present and present.next is not None and prev is not None:
            prev.next = present.next
        
        return head