#Link:https://neetcode.io/problems/number-of-senior-citizens/question
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num = 0
        for i in details:
            if int(i[11:13]) > 60:
                num+=1
        return num