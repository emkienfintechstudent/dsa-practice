class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0 
        r_row = len(matrix) - 1 
        while l_row <= r_row:
            if