class Ex75(object):        
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = 0 # points to start of 1
        p2 = len(nums) - 1 # points to start of 2
        i = 0
        while i <= p2:
            while p2 >= 0 and nums[p2] == 2:
                p2 -= 1
            if i > p2:
                break
            if nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
            else:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
                if nums[i] != 0:
                    # Then re-process the current item
                    continue
                else:
                    nums[i], nums[p1] = nums[p1], nums[i]
                    p1 += 1
            i += 1
        return nums
    '''
    def sortColors(self, nums):    
        A = nums
        n = len(nums)
        p2=n-1
        p0=0
        i = 0
        while i <= p2:            
            while (A[i]==2 and i<p2):
                A[i], A[p2] = A[p2], A[i]
                p2 -= 1
            while (A[i]==0 and i>p0):
                A[i], A[p0] = A[p0], A[i]
                p0 += 1
            i += 1
        print nums
    '''
    '''
    def sortColors(self, nums):
        i = j = 0
        for k in xrange(len(nums)):
            v = nums[k]
            nums[k] = 2
            print 100, nums, v, k
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
    '''
    '''
    // one pass in place solution
    void sortColors(int A[], int n) {
        int n0 = -1, n1 = -1, n2 = -1;
        for (int i = 0; i < n; ++i) {
            if (A[i] == 0) 
            {
                A[++n2] = 2; A[++n1] = 1; A[++n0] = 0;
            }
            else if (A[i] == 1) 
            {
                A[++n2] = 2; A[++n1] = 1;
            }
            else if (A[i] == 2) 
            {
                A[++n2] = 2;
            }
        }
    }
    '''
    
ex75 = Ex75()

nums = [2,2,1,1]
nums = [2,2]
nums = [0,1,0,2,1,0,1]
nums = [1,2,0]
nums = [2,1,0]
nums = [2,2,0]
nums = [2, 1, 0, 1, 2]
print 75, ex75.sortColors(nums)
