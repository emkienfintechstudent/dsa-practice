#link: https://neetcode.io/problems/validate-parentheses/question
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {'}':'{',']':'[',')':'(' }
        for i in s:
            if i in close_to_open:
                if stack and close_to_open[i] == stack [-1]:
                 stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
          
          