from typing import List

class Solution:

    def helper(self, comb)->int:
        count = 0
        c_index, t = comb

        if c_index+1 >= len(self.coins):
            return 0
        
        c_index += 1
        mul = 0

        while t - (self.coins[c_index])*mul <= self.amount and t - (self.coins[c_index])*mul > -1:
            new_t = t - ((self.coins[c_index])*mul)
            if new_t == 0:
                count += 1
            
            if new_t > 0:
                if (c_index, new_t) in self.tracker_dict:
                    count += self.tracker_dict[(c_index, new_t)]
                else:
                    self.tracker_dict[(c_index, new_t)] = self.helper((c_index, new_t))
                    count += self.tracker_dict[(c_index, new_t)]
            mul += 1

            if new_t < 0:
                break

        return count

    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        
        stack = []
        count = 0
        self.tracker_dict = dict()
        coins.sort()
        self.coins = coins
        self.amount = amount 

        t = 0
        c1 = 0
        while coins[c1]*t <= amount+1:
            new_t = amount - coins[c1]*t
            if new_t > 0:
                stack.append((c1, new_t))

            if new_t == 0:
                count+= 1
            t += 1
        
        for comb in stack:
            count += self.helper(comb)
        
        return count
            
