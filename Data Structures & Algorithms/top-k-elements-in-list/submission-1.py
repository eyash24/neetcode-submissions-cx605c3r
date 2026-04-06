from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        li_count_value = []
        for k_,v_ in counter.items():
            li_count_value.append((v_, k_))
        
        li_count_value.sort(reverse=True)
        ret = []
        i=0
        print(k)
        while i < k:
            _, k_ = li_count_value[i]
            ret.append(k_)
            i += 1
        return ret


