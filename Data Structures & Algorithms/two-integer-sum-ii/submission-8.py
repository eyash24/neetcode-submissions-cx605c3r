class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        di = dict()

        for index, n in enumerate(numbers):
            if target - n in di:
                return [di[target-n], index+1]
            di[n] = index+1