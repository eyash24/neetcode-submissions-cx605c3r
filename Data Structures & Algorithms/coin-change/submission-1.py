class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        filtered_coins = [i for i in coins if i <= amount]
        if amount in coins:
            return 1
        
        else:
            flag = True
            tracker = {i:-1 for i in range(1,amount+1)}
            for i in filtered_coins:
                tracker[i] = 1

            for i in tracker:
                c_count = None
                for j in filtered_coins:
                    if i-j == 0:
                        c_count = 1
                    elif i-j > 0 and tracker[i-j] != -1:
                        if c_count is None:
                            c_count = tracker[i-j] + 1
                        else:       
                            c_count = min(c_count, tracker[i-j]+1)
                if c_count is None:
                    tracker[i] = -1
                else:
                    tracker[i] = c_count

        print(tracker)
    

        return tracker[amount]
                
                    
                


