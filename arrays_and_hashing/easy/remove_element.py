#link: https://neetcode.io/problems/remove-element/question?list=allNC
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0 
        lst = []
        for i in nums:
            if i != val:
                nums[count] = i
                count+=1
        return count