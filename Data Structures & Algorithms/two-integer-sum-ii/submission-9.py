class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, len(numbers)-1

        while s < e:
            v = numbers[s] + numbers[e]

            if v == target:
                return [s+1, e+1]
            elif v > target:
                e -= 1
            else:
                s += 1