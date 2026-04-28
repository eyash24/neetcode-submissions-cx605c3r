class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        tracker = dict()
        limit = len(s)
        i = 0
        while i < len(s):
            print(i)
            prev = s[:i]
            curr = int(s[i])
            print(f'\nprev: {prev}\ncurr:{curr}')
            if curr > 0 and curr < 10:
                if curr == 1 or curr == 2:
                    if i+1 < limit:
                        next_l = int(s[i+1])
                        if curr*10 + next_l < 27:
                            ele = prev + str(curr*10+next_l)
                            print('ele: ', ele)
                            print(f'INNER\ntracker[{ele}]: {tracker.get(ele, 1)}\ntracker[{prev}]: {tracker.get(prev, 1)}')
                            count= tracker.get(ele, 1) * tracker.get(prev, 1)
                            tracker[ele] = tracker.get(ele, 0) + count

                elif i+1 < limit and int(s[i+1])==0:
                    return 0

                print(f'Outer:\ntracker[{prev+str(curr)}]: {tracker.get(prev+str(curr), 1)}\ntracker[{prev}]: {tracker.get(prev, 1)}')   
                count_outer = 1*tracker.get(prev, 1)
                tracker[prev+str(curr)] = tracker.get(prev+str(curr), 0) + count_outer
                i += 1
            elif curr == 0:
                print('Encounter Zero')
                if (i+1 < len(s) and int(s[i+1]) == 0) or (i-1 >= 0 and int(s[i-1]) > 2):
                    print('working')
                    return 0
                else:
                    
                    i+=1
            else:
                i+=1
            
            print(tracker)

        return tracker[s]
