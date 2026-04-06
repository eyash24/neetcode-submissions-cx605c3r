from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_row = [row[0] for row in matrix]
        # print(matrix, target, sep='\n')
        row_found = 0
        # finding the row
        row_count = len(first_row)
        l_row, r_row = 0, row_count

        while l_row < r_row:
            mid_row = (l_row + r_row)// 2
            if first_row[mid_row] == target:
                return True

            elif first_row[mid_row] < target:
                if mid_row + 1 < row_count:
                    if first_row[mid_row+1] > target:
                        row_found = mid_row
                        break
                    else:
                        l_row = mid_row + 1
                else:
                    row_found = mid_row
                    break

            elif first_row[mid_row] > target:
                if mid_row - 1 >= 0:
                    r_row = mid_row -1
                else:
                    return False
                
        # print('row_found: ', row_found)
        # after row being found
        row = matrix[row_found]
        limit = len(row) - 1
        l,r = 0, limit

        while l <= r:
            # print('l: ', l, ' r: ', r)
            mid = (l+r) //2
            # print("mid: ", mid, ' mid_ele: ', row[mid])
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid - 1
            elif row[mid] < target:
                l = mid + 1
        else:
            return False