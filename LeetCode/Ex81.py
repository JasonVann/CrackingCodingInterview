class Ex81(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        lr = nums[-1]
        rl = nums[0]
        n = len(nums)
        if n <= 2:
            if target not in nums:
                return -1
            return nums.index(target)
        
        l = 0
        r = n-1
        if nums[-1] > nums[0]:
            p = 0
        else:
            while l <= r:
                p = (l+r)/2
                print 78, p, nums[p], l, r
                if nums[p]> nums[r]:
                    l = p + 1
                else:
                    r = p - 1
                
                print 81, l, r, p
        print 80, p
        if nums[p-1] < target or nums[p] > target:
            return -1
        
        if nums[-1] >= target:
            l = p
            r = n - 1
        else:
            l = 0
            r = p - 1
        print 91, l, r
        while l <= r:
            m = (l + r)/2
            print 99, m, nums[m], target
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            print 104, l, r, m
        return -1
        
    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                return True
            print 67, mid, lo, hi
            print 68, nums[lo], nums[mid], nums[hi]
            if nums[lo] <= nums[mid]:
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
                
            else:
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1               
            print 79, lo, hi
            
        if lo >= n:
            return False
        return nums[lo] == target
        

    def search0(self, nums, target):
        return target in nums
        
ex81 = Ex81()
n = [3,1,1]
t = 1
n = [1,3,1,1,1]
t = 3
print 81, ex81.search(n, t)

