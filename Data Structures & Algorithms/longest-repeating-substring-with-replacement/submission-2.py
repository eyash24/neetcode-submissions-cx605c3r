class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # print("s: ", s, "k: ",k)
        max_count = 1
        limit = len(s)

        for i in range(limit):
            # print(f'\ni: {i}, match:{s[i]}')
            match = s[i]
            start = i

            mid_count = 1
            for j in range(start+1,limit):
                # print(f'j: {j}, ele: {s[j]}, mid_count: {mid_count}')
                if s[j] == match:
                    mid_count += 1
                else:
                    break

            # print(f'final mid_count: {mid_count}')
            end = start + mid_count - 1
            
            right_count = 0
            left_count = 0

            temp_l_k = k
            temp_r_k = k

            if start - 1 >= 0:
                # left_part exist
                # print('\nLeft')
                # print(f'start - 1: {start-1}')
                for l in range(start-1, -1, -1):
                    # print(f"s[{l}]: ",s[l])
                    if s[l] == match:
                        left_count += 1
                    elif temp_l_k > 0:
                        temp_l_k -= 1
                        left_count += 1
                    else:
                        break
                
                left_part = s[start - left_count: start][::-1]
            else:
                # print("No left")
                left_part = None
            
            if end+1 < limit:
                # right part
                # print('\nright')
                # print("end + 1: ", end+1)
                for r in range(end+1, limit):
                    # print(f"s[{r}]: ", s[r])
                    if s[r] == match:
                        right_count += 1
                    elif temp_r_k > 0:
                        temp_r_k -= 1
                        right_count += 1
                    else:
                        break

                right_part = s[end+1: end + right_count+1]
            else:
                right_part = None

            # print('left count: ', left_count, ',right_count: ', right_count)            
            # print('left: ', left_part, '\nright: ', right_part)
            combine_count = 0
            if temp_l_k > 0 and temp_r_k > 0:

                if right_part and left_part:
                # combine 
                    if left_count > right_count:
                        combine_count = left_count
                        to_check = right_part
                        comb_k_left = k - temp_l_k
                    else:
                        combine_count = right_count
                        to_check = left_part
                        comb_k_left = k - temp_r_k
                    
                    for c in range(len(to_check)):
                        if comb_k_left > 0 and to_check[c] != match:
                            comb_k_left -= 1
                            combine_count += 1
                        elif to_check[c] == match:
                            combine_count += 1
                        else:
                            break
                elif right_part:
                    combine_count = right_count
                elif left_part:
                    combine_count = left_count
                else:
                    combine_count = 0
            else:
                combine_count = max(left_count, right_count)

            max_count = max(max_count, mid_count + combine_count)
    
        return max_count
                
    