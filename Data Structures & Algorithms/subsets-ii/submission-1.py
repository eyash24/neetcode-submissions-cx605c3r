class Solution:
    def subsetHelper(self, nums, index, freq):
        print(nums, freq, index)

        if freq not in self.freq_tracker:
            print(f'Adding this num: {nums}')
            self.combi.append(nums.copy())
            self.freq_tracker.append(freq.copy())    
        
        
        for i in range(len(nums)):
            first_ele = nums.pop(0)
            
            next_nums = nums[:index]
            freq[first_ele] -= 1
            if freq[first_ele] == 0:
                del freq[first_ele]
            
            if index >= 1:
                self.subsetHelper(next_nums, index-1, freq)

            nums.append(first_ele)
            freq[first_ele] = freq.get(first_ele,0) + 1
        
        return

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.freq_tracker = []
        self.combi = [[]]

        freq = dict()
        for i in nums:
            freq[i] = freq.get(i, 0)+1

        self.freq_tracker.append(freq.copy())
        self.combi.append(nums.copy())

        self.subsetHelper(nums, len(nums)-1, freq)

        return self.combi
        