class Ex34(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        lo = 0
        hi = len(nums) - 1
        while True:            
            if abs(hi - lo) <= 1:
                print 91, lo, hi
                if nums[lo] != target and nums[hi] != target:
                    return [-1, -1]
                    
                while lo > 0 and nums[lo-1] == target:
                    lo -= 1
                while hi < len(nums) - 1 and nums[hi+1] == target:
                    hi += 1
                if nums[hi] != target:
                    hi -= 1
                if nums[lo] != target:
                    lo += 1
                
                return [lo, hi]
                        
            mid = lo + (hi - lo)/2
            
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = lo + 1
                hi = hi - 1
            print 93, mid, lo, hi
    '''
    def searchRange(self, nums, target):
        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) / 2
                l, r = search(lo, mid), search(mid+1, hi)
                return max(l, r) if -1 in l+r else [l[0], r[1]]
            return [-1, -1]
        return search(0, len(nums)-1)
    '''
    '''
    def searchRange(self, nums, target):
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) / 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]
    '''
    
ex34 = Ex34()
nums = [5, 7, 7, 7, 8, 8]
t = 8
nums = [1,3]
t = 1
print 34, ex34.searchRange(nums, t)

