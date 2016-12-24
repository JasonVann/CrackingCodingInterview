class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        lsum = []
        for i in range(len(nums)):
            if i == 0:
                lsum.append(nums[0])
            else:
                lsum.append(lsum[i-1] + nums[i])
        #print lsum
        self.nums = lsum
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        '''
        res = 0
        while i <= j:
            res += self.nums[i]
            i+=1
        #return sum(self.nums[i:j+1])
        return res
        '''
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i-1]

# Your NumArray object will be instantiated and called as such:
nums = [-2,0,3,-5,2,-1]
numArray = NumArray(nums)
print 303, numArray.sumRange(0, 1)
print 303, numArray.sumRange(1, 2)


