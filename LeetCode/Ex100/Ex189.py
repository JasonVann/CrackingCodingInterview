class Ex189(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k > 0:
            nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]
        '''
        while k > 0:
            e = nums.pop(-1)
            nums.insert(0, e)
            k -= 1
        '''
        '''
        if k > 0:
            if len(nums) % k == 0:
                nums = (nums[k:] + nums[:k])[:]
            else:
                nums = nums[len(nums) - k:] + nums[:k+1]
        #print nums
        '''
        
ex189 = Ex189()
print 189, ex189.rotate([1,2],1)
print 189, ex189.rotate([1,2,3,4,5,6,7],3)
