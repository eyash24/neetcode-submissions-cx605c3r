class Solution:
    def sumHelper(self, index, curr_sum):
        if index == len(self.nums)-1 and curr_sum + self.nums[index] == self.half_sum:
            return True
        elif index == len(self.nums)-1 and curr_sum + self.nums[index] != self.half_sum:
            return False

        sum1 = curr_sum + self.nums[index]
        sum2 = curr_sum

        if sum1 == self.half_sum:
            return True

        else:
            return self.sumHelper(index+1, sum1) or self.sumHelper(index+1, sum2)
         

    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        sum_nums = sum(nums)
        if sum_nums %2 != 0:
            return False
        else:
            self.half_sum = sum_nums / 2
            return self.sumHelper(0, 0)





        
