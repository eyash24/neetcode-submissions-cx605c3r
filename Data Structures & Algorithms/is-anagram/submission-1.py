class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = dict()
        s_u = []
        for e in s:
            if e not in s_u:
                s_count[e] = 1
                s_u.append(e)
            else:
                s_count[e] += 1
        
        t_count = dict()
        t_u = []
        for e in t:
            if e not in t_u:
                t_u.append(e)
                t_count[e] =1
            else:
                t_count[e] += 1
        
        if t_count == s_count:
            return True
        return False


