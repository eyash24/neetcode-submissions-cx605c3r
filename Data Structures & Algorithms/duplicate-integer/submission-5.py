

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_unique = dict()
        for n in nums:
            if n not in dict_unique.keys():
                dict_unique[n] = 1
            else:
                return True
        else:
            return False
        
        