class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = list()
        for i in nums:
            if i not in visited:
                visited.append(i)
            elif i in visited:
                return True
        return False

         