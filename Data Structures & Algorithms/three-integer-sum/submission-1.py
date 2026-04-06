class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        index_dict = dict()
        set_ans = list()
        
        for i,n in enumerate(nums):
            if n not in index_dict.keys():
                index_dict[n] = [i]
            else:
                n_list = index_dict[n]
                n_list.append(i)
                index_dict[n] = n_list
        
        for i, n_1 in enumerate(nums):
            for j, n_2 in enumerate(nums):
                if i == j:
                    continue
                
                sum_n = n_1 + n_2
                req = 0 - sum_n
                
                if req in index_dict.keys():
                    index_list = index_dict[req]
                    available = False
                
                    for l in index_list:
                        if l != i and l != j:
                            available = True

                    if available:
                        ans = [n_1, n_2, req]
                        ans.sort()
                        if ans not in set_ans:
                            set_ans.append(ans)

        return set_ans


                    

                    


