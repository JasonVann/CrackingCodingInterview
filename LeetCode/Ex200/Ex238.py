class Ex238(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # No division
        prod = 1
        count_zero = 0
        for i in nums:
            if i == 0:
                count_zero += 1
            else:
                product *= i
                
        res = []
        if count_zero > 1:
            return [0] * len(nums)
            
        for i in nums:
            if count_zero > 0:
                if i != 0:
                    res.append(0)
                else:
                    res.append(prod)                    
            else:
                res.append(prod/i)
        return res
    '''
    class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
        def productExceptSelf(self, nums):
            p = 1
            n = len(nums)
            output = []
            for i in range(0,n):
                output.append(p)
                p = p * nums[i]
            p = 1
            for i in range(n-1,-1,-1):
                output[i] = output[i] * p
                p = p * nums[i]
            return output
    '''

