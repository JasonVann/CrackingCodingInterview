class Ex213(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        M = [] # max loot
        if len(nums) == 0:
            return sum(M)
        if len(nums) == 1:
            return nums[0]
        M.append(nums[0])
        M.append(max(nums[0], nums[1]))
        take_first = False
        for i in range(2, len(nums)):            
            if i == len(nums) - 1 and take_first:
                break
            if M[i-1] > nums[i] + M[i-2]:
                M.append(M[i-1])
            else:
                if i == 2:
                    take_first = True
                if i == len(nums) - 1 and take_first:
                    M.append(M[i-1])
                else:
                    M.append(nums[i] + M[i-2])
            
        M2 = [] # do not take the 1st
        M2.append(0)
        M2.append(nums[1])
        for i in range(2, len(nums)):            
            if M2[i-1] > nums[i] + M2[i-2]:
                M2.append(M2[i-1])
            else:
                M2.append(nums[i] + M2[i-2])
        
        print 87, M, M2
        return max(M[-1], M2[-1])
        
ex213 = Ex213()
nums = [4, 1, 2]
print 213, ex213.rob(nums)

