class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets.sort()
        filtered_triplets = [
            tr for tr in triplets 
            if (tr[0] <= target[0] and tr[1] <= target[1] and tr[2] <= target[2]) 
            and (tr[0] == target[0] or tr[1] == target[1] or tr[2] == target[2])
        ]
        
        if len(filtered_triplets) < 0:
            return False

        if target in filtered_triplets:
            return True

        i1, i2, i3 = False, False, False

        for tp in filtered_triplets:
            if tp[0] == target[0]:
                i1 = True
            
            if tp[1] == target[1]:
                i2 = True
                
            if tp[2] == target[2]:
                i3 = True
        
        if i1 and i2 and i3:
            return True
        else:
            return False
            


            
        

        
        

        
