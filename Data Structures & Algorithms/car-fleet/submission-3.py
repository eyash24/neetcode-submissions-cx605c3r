class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        fleets = 1
        p_s = list(zip(position, speed))
        p_s.sort()
        p_s = p_s[::-1]
        stack = [p_s[0]]
        ps_prev = p_s[0]

        for i,ps in enumerate(p_s[1:]):
            if ps_prev[-1] >= ps[-1]:
                fleets += 1
                ps_prev = ps
            else:
                x = (ps_prev[0] - ps[0]) / (ps[-1] - ps_prev[-1])
                d = x*(min(ps[-1], ps_prev[-1]))
                if ps_prev[0] + d > target:
                    fleets += 1
                    ps_prev = ps

        return fleets