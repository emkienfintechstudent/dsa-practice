# link: https://leetcode.com/problems/removing-stars-from-a-string/description/
class Solution:
    def removeStars(self, s: str) -> str:
        s = s[::-1]
        skip = 0
        result ='' 
        for i in s:
            if i != '*' and skip ==0:
                result += i
            elif i== '*':
                skip +=1
                continue 
            else :
                skip -=1 
                continue
        return result[::-1]