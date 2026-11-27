class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = dict()

        for n in nums:
            counter[n] = counter.get(n, 0) + 1
            if counter[n] > 1:
                return True
        return False