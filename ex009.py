class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 != 0:
            return nums1[len(nums1)//2]
        return (nums1[len(nums1)//2 - 1] + nums1[len(nums1)//2 ]) / 2
    
# funciona, mas a complexidade tá ruim