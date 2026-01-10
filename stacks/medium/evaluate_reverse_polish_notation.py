# link: https://neetcode.io/problems/evaluate-reverse-polish-notation/question
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst = []
        for i in tokens:
            if i == "+":
                total = lst[-2] + lst[-1]
                lst.pop()
                lst.pop()
                lst.append(total)
            elif i =="*":
                multiple = lst[-2] * lst[-1]
                lst.pop()
                lst.pop()
                lst.append(multiple)
            elif i == "-":
                minus= lst[-2] - lst[-1]
                lst.pop()
                lst.pop()
                lst.append(minus)
            elif i == "/":
                divide = int(lst[-2] / lst[-1])
                lst.pop()
                lst.pop()
                lst.append(divide)
            else:
                lst.append(int(i))
        return lst[0]