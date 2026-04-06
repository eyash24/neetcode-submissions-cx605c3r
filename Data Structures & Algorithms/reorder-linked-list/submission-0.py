class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ll_list = []
        new_head = current_ele = None

        while head:
            ll_list.append(head)
            head = head.next
        
        # val_list = [p.val for p in ll_list]
        # print(val_list)

        if len(ll_list) <2:
            return head
        
        l, r = 0, len(ll_list)-1
        # print(l,r)

        while l <= r:
            # print(l,r)
            if l == 0:
                new_head = ll_list[l]
                current_ele = new_head
                # print(current_ele.val)
            elif l == r:
                # print('r == l')
                current_ele.next = ll_list[r]
                current_ele = current_ele.next
                # print(current_ele.val)
                l += 1
                r -= 1
                continue
            else:
                # print('else, l: ', l)
                current_ele.next = ll_list[l]
                current_ele = current_ele.next
                # print(current_ele.val)
                # print('done')
            
            # print(ll_list[l], ll_list[r])

            current_ele.next = ll_list[r]
            current_ele = current_ele.next
            # print(current_ele.val)
            l+=1
            r-=1
            # print(l,r)
        
        current_ele.next = None
        head = new_head