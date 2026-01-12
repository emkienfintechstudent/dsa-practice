import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        special_chars = string.punctuation
        s=s.replace(" ", "")
        s= s.rstrip(special_chars).lower()
        print(s)
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l] ==s[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
                break
        return True