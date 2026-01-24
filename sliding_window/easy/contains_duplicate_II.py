#link:https://neetcode.io/problems/contains-duplicate-ii/question
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seem = {}
        for i, num in enumerate(nums):
            if num in seem and abs(seem[num] -i ) <= k:
                return True
            else:
                seem[num] =i
        return False