from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict(Counter(nums))
        freq = [[j,i] for i,j in freq.items()]
        freq.sort()
        
        return [ele[1] for ele in freq[-k:]]
