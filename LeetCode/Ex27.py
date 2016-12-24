class Ex27(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        l = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == val:
                while nums[j] == val and j >= i:
                    j -= 1
                if j < i:
                    #print 'b', nums, l, i, j
                    return l
                #print 'c', nums, l, i, j
                nums[i], nums[j] = nums[j], nums[i]
                l += 1
            else:
                l += 1
        
        #print nums, l, i, j
        return l
        
ex27 = Ex27()
nums = [3,3,4,5,6]
#nums = []
print 27, ex27.removeElement(nums, 3)
