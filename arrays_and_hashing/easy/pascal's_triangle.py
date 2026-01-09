# link: https://neetcode.io/problems/pascals-triangle/history
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[1]]
        for i in range(numRows-1):
            num = 0 
            lst_temp =lst[-1].copy()
            lst_temp_2 = [1,1]
            print(lst_temp)
            for j in range(len(lst_temp)-1):
                lst_temp_2.insert(j+1,(lst_temp[j] + lst_temp[j+1]))
            lst.append(lst_temp_2)
        return lst