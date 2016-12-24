class Ex215(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]
        
def iter(nums, l, r):
    # l, r inclusive
    i = l
    p = nums[l]
    for j in range(i+1, r + 1):
        if nums[j] < p:
            print 1883, i, j, nums
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
            print nums, i, j
        #j += 1
    print 1888, nums, i, j
    return i 
    
def DSelect(nums, k):
    l = 0
    r = len(nums) - 1
    while True:
        i = iter(nums, l, r)
        if i < k:
            l = i
            k = k - i
        elif i > k:
            r = i - 1
            #k = k - i
        else:
            break
    
    print 1905, nums, nums[l+k], nums[k], i, k, l, r
    
nums = [5, 2, 1,3,6,4]
#print 353, iter(nums, 0, 5)   
print 1909, DSelect(nums, 4)       

