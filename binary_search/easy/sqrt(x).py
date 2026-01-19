class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x ==1:
            return x 
        r = int(x/2)
        l= 2
        while l * l <= x:
            l+=1
        return l-1