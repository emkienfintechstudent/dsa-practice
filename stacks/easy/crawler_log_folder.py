# link: https://neetcode.io/problems/crawler-log-folder/question
#solution 1: 
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0 
        for i in logs:
            if i == "../" and count !=0:
                count -=1
            elif i != "./" and i != "../":
                count +=1
            else: continue
        return count

#solution 2 using stack: 
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs :
            if i == "../":
                if stack:
                    stack.pop()
            elif i != "./":
                stack.append(i)
            else: continue
        return len(stack)