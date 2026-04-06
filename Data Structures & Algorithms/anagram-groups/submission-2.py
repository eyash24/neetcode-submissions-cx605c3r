
def concatenate_list(li:list):
    st = ''
    for l in li:
        st += l
    return st

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_dict = dict()
        
        if len(strs) == 0:
            return [strs]
        else:
            for st in strs:
                sorted_st = sorted(st)
                # concatenating to form a str
                key = concatenate_list(sorted_st)
                if key not in counter_dict.keys():
                    counter_dict[key] = [st]
                else:
                    li = counter_dict[key]
                    li.append(st)
                    counter_dict[key] = li
            return list(counter_dict.values())