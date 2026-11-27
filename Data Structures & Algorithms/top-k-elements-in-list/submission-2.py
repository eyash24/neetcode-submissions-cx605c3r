class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = dict()

        for n in nums:
            di[n] = di.get(n, 0) + 1
        
        li = [[v,key] for key,v in di.items()]
        li.sort(reverse=True)

        return [arr[1] for arr in li[:k]]