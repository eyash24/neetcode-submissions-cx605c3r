def getFreq(string: str) -> dict:
    track = dict()
    for s in string:
        if s in track:
            track[s] += 1
        else:
            track[s] = 1
    
    return track

def dictMember(dict_1: dict, dict_2: dict) -> bool:
    for k,v in dict_1.items():
        if k not in dict_2:
            return False
        elif dict_2[k] < v:
            return False
    return True



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # print("s: ", s, "t: ", t)
        s_counter = getFreq(s)
        t_counter = getFreq(t)
        limit = len(s)

        if dictMember(t_counter, s_counter) is False:
            return ""
        else:
            min_length = limit
            min_str = s

            target_set = set(t)
            for ct in target_set:
                for index, char in enumerate(s):
                    if ct == char:
                        l=0
                        prev = current = s[l:index+1]
                        # print('Current: ', current)
                        while l < index+1:
                            if dictMember(t_counter, getFreq(current)):
                                # print('taking new ')
                                l+= 1
                                prev = current
                                current = s[l: index+1]
                                # print('New current: ', current)
                            else:
                                # print('Taking prev')
                                prev_length = index - l + 1
                                if dictMember(t_counter, getFreq(prev)) and prev_length < min_length:
                                    min_length = prev_length
                                    min_str = prev
                                break
                        else:
                            # print('Taking prev')
                            prev_length = index - l + 1
                            if dictMember(t_counter, getFreq(prev)) and prev_length < min_length:
                                min_length = prev_length
                                min_str = prev
                        
            return min_str