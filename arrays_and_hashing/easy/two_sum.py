#link:https://neetcode.io/problems/two-integer-sum/question
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_1 = 0
        num_2= 1
        lst= []
        while num_2 < len(nums): 
            print(nums[num_1] + nums[num_2])
            if nums[num_1] + nums[num_2] == target:
                lst.append(num_1)
                lst.append(num_2)
                break
            elif num_2 == len(nums)-1:
                num_1 +=1 
                num_2= num_1 + 1 
            else:
                num_2 +=1
        return lst

