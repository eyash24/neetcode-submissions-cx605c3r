from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        box = [[0]*n for _ in range(n)]

        max_day = [0]*n

        for i in range(n-1):
            for j in range(i+1,n):
                if i >= 2:
                    add = max(max_day[:i-1])
                else:
                    add = 0
                
                if prices[i] < prices[j]:
                    box[i][j] = add + prices[j] - prices[i]
                else:
                    box[i][j] = add
                
                max_day[j] = max(max_day[j], box[i][j])

        return max(max_day)