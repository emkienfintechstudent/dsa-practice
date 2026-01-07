# link: https://neetcode.io/problems/score-of-a-string/question?list=allNC
class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s) -1):
            if ord(s[i]) > ord(s[i+1]):
             sum = sum + ord(s[i]) - ord(s[i+1])
            else:
                sum = sum +ord(s[i+1])- ord(s[i]) 
        return sum