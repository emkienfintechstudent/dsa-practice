link: https://neetcode.io/problems/baseball-game/question
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst = []
        for i in operations:
            if i == "+":
                lst.append(int(lst[-1]+lst[-2]))
            elif i =="D":
                lst.append(lst[-1]*2)
            elif i =="C":
                lst.pop()
            else:
                lst.append(int(i))
        print(lst)
        return sum(lst)