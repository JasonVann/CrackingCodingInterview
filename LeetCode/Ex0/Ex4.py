class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = 0
        l2 = 0
        r1 = len(nums1)
        r2 = r1
        while True:
            if nums[r1] <= num2[l2]:
                return (nums[r1] + nums2[l2]) / 2
            elif nums[l1] >= num2[r2]:
                return (nums[l1] + nums2[r2]) / 2
            else:
                
