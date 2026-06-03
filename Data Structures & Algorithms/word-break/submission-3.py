class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = {i:len(i) for i in wordDict}
        tracker = [-1]*(len(s)+1)
        
        proceed = False

        for w in wordDict:
            if s.startswith(w):
                tracker[0] = 1
                proceed = True
        
        if not proceed:
            return False
        
        else:
            
            start = min(wordDict.values())
            for i in range(start,len(s)+1):
                for w,l in wordDict.items():
                    print('cal: ', i-l)
                    print('start flag: ', s[i-l: i].startswith(w))
                    print('tracker val: ',tracker[i-l])
                    if i-l >=0 and s[i-l: i].startswith(w) and tracker[i-l] == 1:
                        tracker[i]= 1
                        continue 
            print(tracker)
            if tracker[-1] == 1:
                return True
            else:
                return False
            
            

            


            
