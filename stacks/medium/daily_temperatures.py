#link: https://neetcode.io/problems/daily-temperatures/question
#Using brute force: 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst = [0] * len(temperatures)
        for i in range(len(temperatures)-1):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    lst[i]= j - i
                    break
        
        
        return lst
#Using stack: 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res