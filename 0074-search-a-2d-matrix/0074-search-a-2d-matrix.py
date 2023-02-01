class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = (len(matrix) * len(matrix[0])) - 1
        col = len(matrix[0])
        while(l <= h):
            mid = l + ((h - l) // 2)
            x = mid // col
            y = mid % col
            if target > matrix[x][y]:
                l = mid + 1   
            elif target == matrix[x][y]:
                return True
            else:
                h = mid - 1
        return False
               
                    
                
        