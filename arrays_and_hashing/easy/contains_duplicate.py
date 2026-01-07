#link: https://neetcode.io/problems/duplicate-integer/question?list=allNC
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums) > len(nums_set):
            return True
        else:
            return False