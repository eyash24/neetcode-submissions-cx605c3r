class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        # finding right_max
        right_max = []
        reverse_prices = prices[::-1]
        r_max = reverse_prices[0]
        for p in reverse_prices[1:]:
            right_max.append(r_max)
            r_max = max(r_max, p)
        right_max = right_max[::-1]

        max_profit = 0
        for i,p in enumerate(prices[:-1]):
            if p < right_max[i]:
                max_profit = max(right_max[i] - p, max_profit)
        
        return max_profit

