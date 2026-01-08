# link : https://neetcode.io/problems/append-characters-to-string-to-make-subsequence/question?list=allNC
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_index = 0
        t_index = 0
        while t_index < len(t) and s_index < len(s):
            if s[s_index] == t[t_index]:
                t_index +=1 
            s_index +=1
        return len(t) - t_index