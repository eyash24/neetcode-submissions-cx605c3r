class Solution:
    def setHelper(self, nums):
        if len(nums) == 1:
            return None
        else:
            ll = []
            for i in range(len(nums)):
                cropped_nums = nums[:-1]
                cropped_nums.sort()
                ll.append(cropped_nums)
                ret = self.setHelper(cropped_nums)
                if ret:
                    for i in ret:
                        if i not in ll:
                            ll.append(i)
                nums.append(nums[0])
                nums.pop(0)
        return ll


    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums, []]
        else:
            ll = []
            for i in range(len(nums)):
                cropped_nums = nums[:-1]
                cropped_nums.sort()
                ll.append(cropped_nums)
                ret = self.setHelper(cropped_nums)
                print(ret)
                if ret:
                    for i in ret:
                        if i not in ll:
                            ll.append(i)
                # rotate array
                nums.append(nums[0])
                nums.pop(0)
        
        print(ll)
        ll += [[]] + [nums]
        ll.sort()
        
        return ll




        