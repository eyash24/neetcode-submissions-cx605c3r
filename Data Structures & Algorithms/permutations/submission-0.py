class Solution:
    def permutateHelper(self, nums, index):
        print(f'nums: {nums}, index: {index}')
        if index == len(nums)- 1:
            self.combi.append(nums.copy())
            return 
        else:
            nums_prefix = nums[:index]
            rotate_arr = nums[index:]
            for i in range(len(nums)-index):
                first_ele = rotate_arr.pop(0)
                rotate_arr.append(first_ele)
                nums_next = nums_prefix + rotate_arr
                self.permutateHelper(nums_next, index+1)
            return 

        

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.combi = []

        self.permutateHelper(nums, 0)
        print(self.combi)
        return self.combi
