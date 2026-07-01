from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        track = [i-j for i,j in zip(gas,cost)]
        if sum(track) < 0:
            return -1

        if len(track) == 1:
            if track[0] >= 0:
                return 0
            else:
                return -1

        
        i = 0
        while i < len(track):
            if track[i] <= 0:
                i+=1
            else:
                # print(f'exp start: {i}')
                
                start = i
                profit = 0
                loss = 0
                flag = True
                # print(len(track))
                for j in range(len(track)):
                    index = (i+j) % len(track)
                    # print('i+j: ', i+j)
                    # print('index: ', index)
                    if track[index] >= 0:
                        profit += track[index]
                    else:
                        loss += track[index]*-1
                    # print(f'profit: {profit}, loss:{loss}')

                    if profit < loss:        
                        # print('profit < less , breaking')
                        flag = False
                        break
                
                if not flag:
                    i += 1
                    
                else:                    
                    return start
        