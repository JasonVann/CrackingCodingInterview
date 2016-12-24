class Ex152(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = [(nums[0], nums[0], nums[0])]
        for i in range(1, len(nums)):
            a = A[i-1][0] * nums[i]           
            if a == 0:
                a = nums[i]
            if A[i-1][1] * nums[i] == 0:
                b = A[i-1][2] * nums[i]
            else:
                b = max(A[i-1][1] * nums[i], A[i-1][2] * nums[i])
            c = nums[i]
            A.append((a,b, c))
            
        max_v = nums[0]
        for (a,b, c) in A:
            if a > max_v or b > max_v or c > max_v:
                max_v = max(a, b, c)
        print 70, A
        
        return max_v
        
    def maxProduct0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = [(nums[0], nums[0])]
        for i in range(1, len(nums)):
            a = A[i-1][0] * nums[i]           
            if a == 0:
                a = nums[i]
            b = max(A[i-1][1] * nums[i], nums[i])
            A.append((a,b))
            
        max_v = nums[0]
        for (a,b) in A:
            if a > max_v or b > max_v:
                max_v = max(a, b)
        print 70, A
        
        nums.reverse()
        A = [(nums[0], nums[0])]
        for i in range(1, len(nums)):
            a = A[i-1][0] * nums[i]           
            if a == 0:
                a = nums[i]
            b = max(A[i-1][1] * nums[i], nums[i])
            A.append((a,b))
            
        print 79, A
        for (a,b) in A:
            if a > max_v or b > max_v:
                max_v = max(a, b)
                
        return max_v
        
ex152 = Ex152()
nums = [-1, -2, -3, 0]
nums = [2,-5,-2,-4,3]
nums = [1,0,-1,2,3,-5,-2]
#print 152, ex152.maxProduct(nums)

