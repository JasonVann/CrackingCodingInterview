
class Ex283(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        for j in range(1, len(nums)):
            if nums[i] == 0:
                if nums[j] != 0:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            else:
                i += 1
        print nums
        
ex283 = Ex283()
test1 = [0, 1, 0, 3, 12]
print 283, ex283.moveZeroes(test1) 
