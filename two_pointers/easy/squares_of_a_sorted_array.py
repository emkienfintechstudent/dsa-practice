class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0 
        j = len(nums) - 1 
        lst = []
        while i<=j:
            if abs(nums[i]) >= abs(nums[j]):
                lst.append(nums[i]*nums[i])
                i+=1
            else:
                lst.append(nums[j]*nums[j])
                j-=1
        return lst[::-1]