class Ex198(object):
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
        for i in range(2, len(nums)):
            
            if M[i-1] > nums[i] + M[i-2]:
                M.append(M[i-1])
            else:
                M.append(nums[i] + M[i-2])
                
        return M[-1]

ex198 = Ex198()
nums = []
nums = [0, 0, 0]
print 198, ex198.rob(nums)

