from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_target = Counter(s1)
        window = len(s1)

        for i in range(0, len(s2)-window+1):
            window_counter = Counter(s2[i:i+window])
            if window_counter == counter_target:
                return True
        else:
            return False

        