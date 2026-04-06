class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_list = []
        max_count = 0
        count = 0

        for char in s:
            if char not in char_list:
                char_list.append(char)
                max_count = max(max_count, len(char_list))
            else:
                index = 0
                while char_list[index] != char:
                    index += 1
                char_list = char_list[index+1:]
                char_list.append(char)

        return max_count
            