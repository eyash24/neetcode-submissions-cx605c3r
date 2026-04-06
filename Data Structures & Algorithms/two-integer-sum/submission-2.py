class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_dict = {}
        for index, ele in enumerate(nums):
            if ele not in hash_dict.keys():
                hash_dict[ele] = index
            require = target - ele
            if require in hash_dict.keys():
                require_index = hash_dict[require]
                if require_index == index:
                    continue
                return [require_index, index]

        