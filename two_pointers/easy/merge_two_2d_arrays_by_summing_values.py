class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        lst = []
        i,j = 0,0
        k=1
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] < nums2[j][0]:
                lst.append(nums1[i])
                i+=1
            elif nums1[i][0] > nums2[j][0]:
                 lst.append(nums2[j])
                 j+=1   
            else: 
                lst.append([nums1[i][0],nums1[i][1]+ nums2[j][1]])
                i+=1
                j+=1
        while i < len(nums1):
                lst.append(nums1[i])
                i += 1
            
        while j < len(nums2):
                 lst.append(nums2[j])
                 j += 1
        return lst