class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        
        l = 0
        h = m - 1
        found_row = -1

        while l <= h:
            mid = l + (h-l) // 2
            # print(matrix[mid][0])
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
                if (target > matrix[mid][0]):
                    found_row = mid
            else:
                h = mid -1
                if target < matrix[mid][0] and target > matrix[mid-1][0]:
                    found_row = mid - 1
            
        if found_row != -1:
            row = matrix[found_row]

            l2 = 0
            h2 = n -1

            while l2 <= h2:
                mid2 = l2 + (h2 - l2) // 2
                # print(row[mid2])
                if row[mid2] == target:
                    return True
                elif row[mid2] < target:
                    l2 = mid2 +1
                else:
                    h2 = mid2 -1
            
            return False
        
        return False