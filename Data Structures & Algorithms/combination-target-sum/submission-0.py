class Solution:
    def combiHelper(self, past, number, freq, psum):
        freq[number] = freq.get(number, 0) + 1
        past.append(number)
        psum += number

        print(past, number, freq, psum)
        
        if psum == self.target:
            if freq not in self.freq_tracker:
                self.combi.append(past.copy())
                self.freq_tracker.append(freq.copy())

        elif psum < self.target:
            for j in self.valid_nums:
                res = self.combiHelper(past, j, freq, psum)

        past.pop()
        freq[number]-=1
        if freq.get(number) == 0:
            del freq[number]
        return None


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.combi = []
        self.freq_tracker = []
        self.target = target
        valid_nums = [i for i in nums if i <= target]
        self.valid_nums = valid_nums
        
        for i in valid_nums:
            if i == target:
                self.combi.append([i])
                self.freq_tracker.append({i:1})

            else:
                for j in valid_nums:
                    self.combiHelper([i], j, {i:1}, i)
        
        return self.combi
                    
