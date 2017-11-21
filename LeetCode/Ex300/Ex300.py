class Ex300(object):
    '''
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            m = (i + j) / 2
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size
    '''
    def lengthOfLIS2(self, nums):
        # O(n2)
        if len(nums) == 0:
            return 0
            
        n = len(nums)
        A = [1] * n
        i = 1
        max_idx = 0
        while i < n:
            print 64, nums, A, max_idx, nums[max_idx]
            if nums[i] > nums[max_idx]:
                A[i] = A[max_idx] + 1
                
            else:
                for j in range(i-1, -1, -1):
                    if nums[i] > nums[j] and A[j] + 1 > A[i]:
                        A[i] = A[j] + 1
            if A[i] > A[max_idx] or (A[max_idx] == A[i] and nums[max_idx] > nums[i]):
                max_idx = i
            i += 1
        print 75, A
        return max(A)
    '''
    def merge_count(self, nums, l, mid, r, nums0):
        # Only count adjacent inversion
        count = 0
        i = l
        j = mid + 1
        temp = []
        print 60, nums[l:mid+1], nums[mid+1:r+1], l, mid, r, nums0[l:mid+1], nums0[mid+1:r+1]
        if mid + 1 <= r and nums0[mid] > nums[mid + 1]:
            idx = mid + 1
            while idx <= r and nums0[mid] > nums[idx]:                
                count = 1
                idx += 1
        while i <= mid and j <= r:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i += 1
            else:                
                temp.append(nums[j])
                j += 1
                #count += 1
        #print 71, temp, i, j, mid
        if i <= mid:
            temp += nums[i:mid+1]
        if j <= r:
            temp += nums[j:r+1]
        
        #print 67, nums, l, r, temp, i, j, mid
        nums[l:r+1] = temp
        #print 69, nums
        return count
        
    def merge_sort(self, nums, l, r, nums0):
        if r - l == 1:
            if nums[r] <= nums[l]:
                nums[l], nums[r] = nums[r], nums[l]
                return 1
            else:
                return 0
        if l >= r:
            return 0
        mid = l + (r - l) / 2
        a1 = nums[l:mid+1]
        a2 = nums[mid+1:r+1]
        o1 = nums0[l:mid+1]
        o2 = nums0[mid+1:r+1]
        c1 = self.merge_sort(nums, l, mid, nums0)
        c2 = self.merge_sort(nums, mid + 1, r, nums0)
        c3 = self.merge_count(nums, l, mid, r, nums0)
        print 96, a1, a2, c1, c2, c3, o1, o2
        return c1 + c2 + c3
        
    def lengthOfLIS0(self, nums):
        nums0 = nums[:]
        n = len((nums))
        
        i = self.merge_sort(nums, 0, len(nums) - 1, nums0)
        print 95, nums, nums0, n, i
        return n - i
    '''
ex300 = Ex300()
nums = [4,3,2,1, 5]
nums = [3,1,2]
nums = [10,9,2,5,9,3,7, 101, 18]
#nums = [10,9,2,5,3,7,101,18]
#nums = [10,9,2,5]
nums = [1,3,6,7,9,4,10,5,6]
nums = [10,9,2,5,3,4]
nums = [1,2,3,10, 4,5]
nums = [-3,-2,-1]
print 300, ex300.lengthOfLIS(nums)

