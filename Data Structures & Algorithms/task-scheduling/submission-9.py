from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        count_dict = dict(Counter(tasks))
        max_heap = [(-v,k) for k,v in count_dict.items()]
        
        heapq.heapify(max_heap)
        process = [0]
        index_dict = dict()
        
        
        while len(max_heap) > 0:
            freq, ele = heapq.heappop(max_heap)
            print(freq, ele)
            
            if ele in index_dict.keys():

                last_index = index_dict[ele]
                next_index = last_index + n + 1

                while next_index < len(process) and process[next_index]!= 0:
                    next_index += 1

                if next_index >= len(process):
                    process += [0]*(next_index - len(process)+n)
                
                process[next_index] = ele
                index_dict[ele] = next_index
                freq += 1
                if freq < 0:
                    heapq.heappush(max_heap, (freq, ele))

            else:
                print('new k')
                index = 0
                while index < len(process) and process[index]!= 0:
                    index += 1
                
                if index >= len(process):
                    process += [0]*(index - len(process) + n)
                
                print(index, process)
                process[index] = ele
                index_dict[ele] = index
                print('post addition: ', process)
                freq += 1
                index += 1

                if freq < 0:
                    heapq.heappush(max_heap, (freq, ele))
        
        print(process)
        num_process = len(process)
        while process[num_process-1] == 0:
            num_process -=1
        
        return num_process

                
                                



