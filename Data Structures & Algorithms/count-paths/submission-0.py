class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        box = [[1]*n]*m

        for i in range(m):
            for j in range(n):
                if i-1 >= 0 and j-1 >= 0:
                    box[i][j] = box[i-1][j] + box[i][j-1]

                elif i-1 >= 0 and j-1 < 0:
                    box[i][j] = box[i-1][j]
                
                elif i-1 < 0 and j-1 >= 0:
                    box[i][j] = box[i][j-1]

        return box[m-1][n-1]


