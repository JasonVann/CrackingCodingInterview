
class Ex16(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None
        nums.sort()
        diff = -1
        for i in range(len(nums) - 2):
            lo = i + 1
            hi = len(nums) - 1
                        
            while lo < hi:
                print 66, nums[i], lo, hi, diff
                if diff == -1:
                    diff = abs(nums[i] + nums[lo] + nums[hi] - target)
                    res = [nums[i], nums[lo], nums[hi]]
                else:
                    diff2 = abs(target - nums[i] - nums[hi] - nums[lo])
                    print 74, diff2, nums[i], nums[hi], diff
                    if diff2 < diff:
                        diff = diff2
                        res = [nums[i], nums[lo], nums[hi]]
                        
                    cur_target = (target - nums[i] - nums[hi])
                    if cur_target == (nums[lo]):
                        return target
                    elif cur_target < (nums[lo]):
                        hi-=1
                    else:
                        lo+=1
        print 84, diff, res
        return sum(res)
       
            
ex16 = Ex16()
nums = [1,1,1,0]
target = -100
nums = [0, 0, 0]
target = 1
nums = [-1, 2, 1, -4]
target = 2
nums = [0,2,1,-3]
target = 1
print 16, ex16.threeSumClosest(nums, target)
