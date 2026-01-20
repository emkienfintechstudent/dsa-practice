# link : https://neetcode.io/problems/search-2d-matrix/question
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0 
        r_row = len(matrix) - 1
        while l_row <= r_row:
            m_row = int((l_row + r_row)/2)
            if matrix[m_row][0] <=target <=matrix[m_row][-1]:
                break
            elif target<matrix[m_row][0]:
                r_row = m_row -1 
            else:
                l_row = m_row +1
        string= matrix[m_row]
        l_col, r_col = 0 , len(matrix[m_row])-1

        while l_col <=r_col:
            m = int((l_col+r_col)/2)
            if string[m] == target:
                return True
            elif string[m] > target:
                r_col = m-1 
            else:
                l_col=m+1 
        return False