class Solution:

    def encode(self, strs: list[str]) -> str:
        prefix = []
        suffix = ""
        for s in strs:
            prefix.append(len(s))
            suffix += s
        prefix = str(prefix)
        pre_len = len(prefix)
        return str(pre_len) + prefix + suffix


    def decode(self, s: str) -> list[str]:

        if s == "2[]":
            return []
            
        pre_len = ""
        index = 0
        while s[index]!="[":
            pre_len += s[index]
            index += 1
        
        pre_len = int(pre_len)
        prefix = s[index:index+pre_len]
        prefix = [int(n.strip()) for n in prefix[1:-1].split(',')]
        suffix = s[index+pre_len:]

        suff_list = []
        index = index+pre_len
        for pre in prefix:
            if pre == 0:
                suff_list.append("")
                continue
            suff_list.append(s[index: index+pre])
            index += pre

        return suff_list