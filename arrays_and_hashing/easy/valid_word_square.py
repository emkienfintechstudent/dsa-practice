#link: https://neetcode.io/problems/valid-word-square/question
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        index = 0 
        check = False
        while index < len(words[0]):
            text = ''
            for i in words: 
                if index >=len(i):
                    continue
                text += i[index]
            if text == words[index]:
                check = True
            else:
                check = False
                break
            index +=1
        return check