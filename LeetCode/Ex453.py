# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Ex453(object):
    def minMoves0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n)
        a = min(nums)
        res = 0
        for i in range(len(nums)):
            cur = nums[i] - a
            res += cur            
        return res
        
    def minMoves0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #O(nlogn)
        nums.sort()
        res = 0
        for i in range(len(nums)):
            cur = nums[i] - nums[0]
            res += cur            
        return res
        
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n2)
        nums.sort()
        res = 0
        last_cur = 0
        cur_sum = 0
        i_max = len(nums) - 1
        i = 0
        while True:
            incr = nums[i_max] - nums[i]
            if incr == 0:
                break
            for j in range(len(nums)):
                if j != i_max:
                    nums[j] += incr
            res += incr
            i_max -= 1
            #i += 1
        return res
    '''
    return sum(nums) - len(nums) * min(nums)
    '''

