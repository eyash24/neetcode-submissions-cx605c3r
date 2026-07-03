class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        box = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text2[i-1] == text1[j-1]:
                    box[i][j] = box[i-1][j-1] + 1
                else:
                    box[i][j] = max(box[i-1][j], box[i][j-1])
        
        return box[n][m]
            



