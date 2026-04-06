from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for c in counter:
            if counter[c]> 1:
                return True
        return False
        