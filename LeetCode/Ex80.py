class Ex80(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """      
        
        n = len(nums)
        if n <= 2:
            return n
        p1 = 1        
        p2 = n - 1
        i = 1
        cur = nums[0]
        to_remove = False
        #for i in range(n-1):
        while i < n:
            if cur != nums[i]:
                to_remove = False
                cur = nums[i]
                nums[i], nums[p1] = None, nums[i]
                #nums[i] = None
                p1 += 1
                i += 1
            else:
                if not to_remove and cur == nums[i]:                
                    nums[p1] = nums[i]
                    if p1 != i:
                        nums[i] = None
                    p1 += 1
                    i += 1
                    to_remove = True
                #if to_remove and cur == nums[i]:
                else:
                    # Then set to null
                    nums[i] = None
                    i += 1
        print nums
        return p1
    '''
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for (int n : nums)
            if (i < 2 || n > nums[i - 2])
                nums[i++] = n;
        return i;
    }
    '''
    
ex80 = Ex80()
nums = [1,1,1,2,2,2,3]
#nums = [1,2,2]
print 80, ex80.removeDuplicates(nums)

