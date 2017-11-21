class Ex55(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        A = [0] * n
        A[0] = 1
        max_j = 0
        for i in range(n):
            cur = nums[i]
            if A[i] == 0:
                continue
            if i + cur <= max_j:
                continue
            for j in range(max_j+1, i + cur + 1):                
                if j < n:
                    A[j] = 1
            if i + cur > max_j:
                max_j = i + cur
        #print A
        return A[-1] == 1
    '''
    bool canJump(int A[], int n) {
        int i = 0;
        for (int reach = 0; i < n && i <= reach; ++i)
            reach = max(i + A[i], reach);
        return i == n;
    }
    '''

