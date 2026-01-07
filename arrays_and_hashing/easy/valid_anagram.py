#link: https://neetcode.io/problems/is-anagram/question
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst_s = sorted(list(s))
        lst_t = sorted(list(t))
        if len(lst_s) != len(lst_t):
            return False
        else: 
            for i in range(len(lst_s)):
                if lst_s[i] != lst_t[i]:
                    return False
            else:
                return True