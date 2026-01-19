# link: https://neetcode.io/problems/guess-number-higher-or-lower/question?list=neetcode250
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = 2147483647
        while guess(n) !=0:
            if(guess(n)) == -1:
                r = n 
                n = int(l/2 + r/2)
            else:
                l = n
                n = int(l/2 + r/2)
        return int(n)