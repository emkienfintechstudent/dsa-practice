#link: https://neetcode.io/problems/max-consecutive-ones/question
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        largest = 0 
        sum =0
        for i in nums:
            if i ==1:
                sum +=1
            else:
                sum =0
            if sum > largest:
                largest = sum
        return largest