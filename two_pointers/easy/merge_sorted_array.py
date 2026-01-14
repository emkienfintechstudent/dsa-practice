class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j =0,0
        while i < m and j <= n -1:
            if nums1[i]> nums2[j]:
                for k in range(m,i-1,-1):
                        nums1[k], nums1[k+1]= nums1[k+1], nums1[k]
                nums1[i] = nums2[j]
                j+=1
            elif nums1[i] == 0:
                nums1[i] = nums2[j]
                j+=1
            print(nums1)
            i+=1

