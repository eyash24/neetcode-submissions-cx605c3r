class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # grps = []
        hand.sort()

        while hand:
            ele = hand.pop(0)
            # print(ele)
            # group = [ele]
            # print('hand: ', hand)
            for i in range(1,groupSize):
                if ele + i in hand:
                    # group.append(ele+i)
                    hand.remove(ele+i)
                else:
                    # print(grps, group, sep='\n')
                    return False
            
        # print(grps)
        return True
            


