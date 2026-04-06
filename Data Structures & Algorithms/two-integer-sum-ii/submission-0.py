class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict_ele = {}
        
        for i,n in enumerate(numbers):
            req_num = target - n
            if req_num in dict_ele.keys():
                index = dict_ele[req_num]
                return [index+1, i+1]
            else:
                dict_ele[n] = i
            