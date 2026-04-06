class Solution:

    def encode(self, strs: List[str]) -> str:
        len_track = []
        for s in strs:
            len_track.append(len(s))
        
        str_val = "".join(strs)
        return str(len_track) + "2001[" + str_val +']'

    def decode(self, s: str) -> List[str]:
        if len(s) == 8:
            return []
        # print(s)
        li, _, strs = s[:-1].partition('2001[')
        # print(li, strs)

        if ',' in li:
            len_track = [int(i) for i in li[1:-1].split(", ")]
        else:
            len_track = [int(li[1:-1])]
        # print(len_track)

        list_strs = []

        start = 0
        for length in len_track:
            # print(length, type(length))
            segment = strs[start: start+length]
            # print(segment)
            list_strs.append(segment)
            start += length
        
        return list_strs