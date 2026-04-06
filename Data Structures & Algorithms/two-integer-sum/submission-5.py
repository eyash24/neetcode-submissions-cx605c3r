class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = []

        for i,n in enumerate(nums):
            req = target-n
            if req in checked:
                j = checked.index(req)
                return [j,i]
            else:
                checked.append(n)