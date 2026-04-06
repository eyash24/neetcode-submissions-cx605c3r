class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        # left max
        left_max = []
        l_max = height[0]
        for h in height[1:]:
            left_max.append(l_max)
            l_max = max(h, l_max)

        # right max
        right_max = []
        r_max = height[-1]
        height_reverse = height[::-1]
        for h in height_reverse[1:]:
            right_max.append(r_max)
            r_max = max(r_max, h)

        right_max = right_max[::-1]
        
        # print(left_max)
        # print(right_max)
        
        quantity = 0
        for i,h in enumerate(height[1:-1]):
            if left_max[i] > h and right_max[i] > h:
                quantity += max(min(left_max[i], right_max[i]) - h, 0)
        
        return quantity 