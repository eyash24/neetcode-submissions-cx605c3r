class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '[]'
        return str([len(s) for s in strs]) + "".join(strs)

    def decode(self, s: str) -> List[str]:

        if s == '[]':
            return []
        l_start, l_end = 1, s.index(']')
        len_list = [int(ln) for ln in s[l_start: l_end].split(",")]
        string = s[l_end+1:]

        l_string = []
        index = 0
        for ln in len_list:
            l_string.append(string[index:index+ln])
            index = index+ln

        return l_string

