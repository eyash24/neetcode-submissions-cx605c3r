class Solution:
    def trap(self, height: List[int]) -> int:
        start_max, end_max = [height[0]], [height[-1]]
        s_max, e_max = -1, -1
        water = 0
        len_h = len(height)
        h_rev = height[::-1]

        for i in range(1, len_h):
            start_max.append(max(height[i], start_max[-1]))
            end_max.append(max(h_rev[i], end_max[-1]))

        end_max = end_max[::-1]

        for k in range(1, len_h-1):
            l, r = start_max[k], end_max[k]
            if l == 0 or r == 0:
                continue
            w = min(l,r) - height[k]
            if w > 0:
                water += w

        return water