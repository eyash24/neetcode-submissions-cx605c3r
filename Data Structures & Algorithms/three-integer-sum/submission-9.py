class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        len_nums = len(nums)
        i = 0
        res = []
        while i < len_nums:
            target = nums[i] * -1
            s, e = i+1, len_nums-1

            while s < e:
                s_e_sum = nums[s] + nums[e]
                if s_e_sum == target:
                    res.append([nums[i], nums[s], nums[e]])
                    j = 0
                    while s+j < e and nums[s+j] == nums[s]:
                        j += 1
                    s += j
                    k = 0
                    while e-k > s and nums[e-k] == nums[e]:
                        k += 1
                    e -= k
                elif s_e_sum < target:
                    j = 0
                    while s+j < e and nums[s+j] == nums[s]:
                        j += 1
                    s += j
                else:
                    k = 0
                    while e-k > s and nums[e-k] == nums[e]:
                        k += 1
                    e -= k
            t = 0
            while i+t < len_nums and nums[i+t] == nums[i]:
                t += 1
            i += t
        return res
                    