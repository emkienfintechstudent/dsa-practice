# link: https://neetcode.io/problems/string-matching-in-an-array/question?list=allNC
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        lst = []
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[j] in words[i] and and words[j] not in lst:
                    lst.append(words[j])
                elif words[i] in words[j] and words[i] not in lst:
                    lst.append(words[i])

        return lst