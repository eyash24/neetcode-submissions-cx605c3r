class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = dict()
        for s in strs:
            s_sorted = ''.join(sorted(s))
            di[s_sorted] = di.get(s_sorted, []) + [s]

        return [li for li in di.values()]