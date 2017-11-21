class Ex35(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo)/2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid
                
        if nums[lo] < target:
            #if lo + 1 < len(nums) and nums[lo + 1] > target:            
            return lo + 1
        if nums[hi] < target:
            #if hi + 1 < len(nums) and nums[hi + 1] > target:            
            return hi + 1            
        return lo

