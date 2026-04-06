from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # dict_index = {}
        # unique_sol = []

        # for i,n in nums:
        #     if n in dict_index.keys():
        #         dict_index[n] += [i]
        #     else:
        #         dict_index[n] = [i]
        
        # target = 0
        # for i,n1 in enumerate(nums):
        #     for j,n2 in enumerate(nums):

        set_unique = list(set(nums))
        freq = dict(Counter(nums))
        sol_list = []

        for i in nums:
            for j in nums:
                if i==j and freq[j] >=2:
                    req = 0-i-j
                    if req in set_unique:
                        if (req == i and freq[i] >=3) or (req != i and req in freq.keys()):
                            li = [i,j,req]
                            li.sort()
                            if li not in sol_list:
                                sol_list.append(li)
                elif i!=j:
                    req = 0-i-j
                    if req in set_unique:
                        if (req == i and freq[i] >= 2) or (req == j and freq[j] >= 2) or (req != i and req != j):
                            li = [i,j,req]
                            li.sort()
                            if li not in sol_list:
                                sol_list.append(li)
        return sol_list







                
        
