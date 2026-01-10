# link:https://leetcode.com/problems/make-the-string-great/description/
class Solution:
    def makeGood(self, s: str) -> str:
        x,y = 0,1
        while x < len(s)-1 :
            if s[x].isupper() and s[y].islower() and s[x].lower() == s[y].lower():
                s = s[:x] + s[y+1:]
                x,y = 0,1
            elif s[x].islower() and s[y].isupper() and s[x].lower() == s[y].lower():
                s = s[:x] + s[y+1:]
                x,y = 0,1
            else:
                x+=1
                y+=1
        return s