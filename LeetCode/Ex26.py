class Ex26(object):
    '''
    def removeDuplicates(self, nums):
        count = 0;
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                print 62, nums, i, count
                nums[i-count] = nums[i]
        print nums
        return len(nums) - count
    '''
    '''
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for (int n : nums)
            if (i == 0 || n > nums[i-1])
                nums[i++] = n;
        return i;
    }
    '''
    '''
    # !!! Two-pointer sol
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                
                i += 1
                nums[i] = nums[j]
                j += 1
                
            else:
                j += 1
        print 87, nums
        return i + 1
    '''
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)
        i = 1
        j = 1
        count = 0
        last = nums[0] - 1
        #for j in range(1, len(nums)):
        while i < len(nums):
            if nums[i] <= nums[i - 1] or nums[i] <= last:
                while j < len(nums) -1 and (nums[j] == nums[i] or nums[j] == nums[i-1]):
                    j += 1
                if j == len(nums):
                    break
                if nums[j] != nums[i] and nums[j] != nums[i-1]:
                    last = nums[i]
                    nums[i] = nums[j]                
                    j += 1
                else:
                    last = nums[i-1]
                i += 1
                count += 1
            else:
                last = nums[i]
                i += 1
                j += 1
        count2 = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                break
            if nums[i] != nums[i-1]:
                count2 += 1
        print count, nums
        return count2
        
    # O(n^2)
    def removeDuplicates_n2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        i = 1
        j = 0
        j_max = len(nums) - 1
        while i < len(nums) and i <= j_max:
            if nums[i] == nums[i - 1]:
                j2 = i
                #print 'a', nums, j_max
                while j2 < j_max:
                    nums[j2] = nums[j2+1]
                    j2 += 1
                nums[j_max] = nums[i-1]
                j_max -= 1
                #print 'b', nums, j_max, i
                i -= 1
            i += 1
        #print nums
        for l in range(len(nums) - 1):
            if nums[l] >= nums[l + 1]:
                return l + 1
        return len(nums)
    
                
    def removeDuplicates3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        i, j = 1, 1
        to_swap = False
        is_dup = False
        current_num = nums[0]
        while i < len(nums) - 1:            
            while j < len(nums) -1 and nums[j] == current_num:
                j += 1
                #to_swap = True
            print 'a', nums, i, j, current_num
            if nums[i] <> current_num:
                #to_swap = False
                current_num = nums[i]
                i += 1
                continue
            if current_num == nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                to_swap = False
            if nums[i] == nums[i-1]:
                i -= 1
            i += 1
        print nums, i, j
        for l in range(len(nums) - 1):
            if nums[l] >= nums[l + 1]:
                return l
        
        
    # This doesn't keep the order
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        j = len(nums) - 1
        i = 1
        c = 0
        while i < len(nums):
            if nums[i] == nums[i-1]:
                print 'a', nums, i, j
                while nums[j] == nums[i] and j >= i:
                    j -= 1
                    c += 1
                if j < i:
                    print 'b', nums, i, j,c
                    return len(nums) - c
                print 'c', nums, i, j,c
                nums[i], nums[j] = nums[j], nums[i]
                c += 1
            i += 1
        print nums, i, j, c
        #return i - (len(nums) - 1 - j)
        return len(nums) - c
        
ex26 = Ex26()
'''
print 26, ex26.removeDuplicates(nums)
print 26, ex26.removeDuplicates([1,1,1,2])
print 26, ex26.removeDuplicates([1,2,3,4])
print 26, ex26.removeDuplicates([1, 1, 2,2,3, 3, 4,5,5])
'''
