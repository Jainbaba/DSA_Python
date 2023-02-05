class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = (len(matrix) * len(matrix[0])) - 1
        col = len(matrix[0])
        while(l <= h):
            mid = l + ((h - l) // 2)
            if target > matrix[mid // col][mid % col]:
                l = mid + 1   
            elif target == matrix[mid // col][mid % col]:
                return True
            else:
                h = mid - 1
        return False
               
                    
                
        