class Solution:
    def combiHelper(self, past, number, sum_past, candidates, freq):
        freq[number] = freq.get(number, 0) + 1
        sum_past += number
        past.append(number)
        # print(f'\nCombi helper\nfreq:{freq}\npast:{past}\nsum_past:{sum_past}')

        if sum_past == self.target and freq not in self.freq_tracker:
            self.combi.append(past.copy())
            self.freq_tracker.append(freq.copy())
            print('---- Answer found: ', past)

        elif sum_past < self.target:
            for i in range(len(candidates)):
                next_cand = candidates[i+1:] if i+1 < len(candidates) else []
                self.combiHelper(past, candidates[i], sum_past, next_cand, freq)
        
        past.pop()
        freq[number] -= 1
        if freq[number] == 0:
            del freq[number]
        
        return 

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        valid_candidate = [i for i in candidates if i <= target]
        print(valid_candidate)
        valid_candidate.sort()
        self.combi = []
        self.freq_tracker = []
        self.target = target

        print(valid_candidate)


        for i in range(len(valid_candidate)):
            next_cand = valid_candidate[i+1:] if i+1 < len(valid_candidate) else []
            print(f'Number: {valid_candidate[i]}, next_cand:{next_cand}')
            if valid_candidate[i] == self.target and {valid_candidate[i]:1} not in self.freq_tracker:
                self.combi.append([valid_candidate[i]])
                self.freq_tracker.append({valid_candidate[i]:1})
            else:
                self.combiHelper([], valid_candidate[i], 0, next_cand, dict())
        print(self.combi)
        return self.combi



