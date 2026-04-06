class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            if target - num in numbers[i+1:]:
                j = numbers.index(target-num)
                return [i+1, j+1]
            
            
        