class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = dict()
        for index, n in enumerate(nums):
            index2 = di.get(target-n, -1)
            di[n] = index
            if index2 != -1:
                return [min(index, index2), max(index, index2)]
