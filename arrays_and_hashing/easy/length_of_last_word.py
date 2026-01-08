# link:https://neetcode.io/problems/length-of-last-word/solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s[::-1]
        check_space_2 = False
        num = 0
        for i in s:
            if i == ' ' and check_space_2 is False:
                continue
            if i == ' ': 
                break
            else: 
                num +=1 
                check_space_2 = True
        return num
