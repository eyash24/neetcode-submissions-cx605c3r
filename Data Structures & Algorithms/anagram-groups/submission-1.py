from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        start = 1

        for string in strs:
            # generating unique list 
            set_string = set(string)

            # generating frequency_list
            string_freq = Counter(string)

            if start == 1:
                start = 0
                anagrams.append([string])
                continue

            found = 0
            for sublist in anagrams:
                check_word = sublist[0]
                check_word_freq = Counter(check_word)
                if set(check_word) == set_string and check_word_freq == string_freq:
                    
                    sublist.append(string)
                    found = 1
                    break

            if found == 0:
                anagrams.append([string])
        
        return anagrams
            
        
                
        