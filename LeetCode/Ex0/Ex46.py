class Ex46(object):
    def fac(self, n):
        if n == 1:
            return 1
        return n * self.fac(n - 1)
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        res = []
        nums.sort()
        nums0 = nums[:]
        temp = []
        n = len(nums)
        #res.append(nums)
        max_l = self.fac(n)
        max_n = nums[-1]
        stack = []
        temp = [[nums[0]]]
        #while len(res) < max_l:  
        for i in range(1, n):
            num = nums[i]
            new_temp = []
            for block in temp:
                j = 0

                while j <= len(block):
                    #block2 = block[:]
                    #block2.insert(j, num)
                    block2 = block[:j] + [num] + block[j:]
                    new_temp.append(block2)
                    if i == n-1:
                        res.append(block2)
                    j += 1
            temp = new_temp
                            
        return res
        
    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Incomplete
        res = []
        nums.sort()
        nums0 = nums[:]
        temp = []
        n = len(nums)
        res.append(nums)
        max_l = self.fac(n)
        max_n = nums[-1]
        i = 1
        temp = nums
        j = n - 1
        k = 1
        fixed = nums[:-1]
        avail = [nums[-1]]
        temp = [[nums[-1]]]
        last_lead = 0
        while len(res) < max_l:  
            
            #if n - len(fixed) == 1:
            if len(fixed) == 0:
                fixed = nums0[:]
                fixed[last_lead+1], fixed[last_lead] = fixed[last_lead], fixed[last_lead+1]
                last_lead += 1
                
            new_e = fixed.pop(-1)
            avail.append(new_e)
            new_temp = []
            for block in temp:
                i = 1

                while i <= len(block):
                    block2 = block[:]
                    block2.insert(i, new_e)
                    new_temp.append(block2)
                    res.append(fixed + block2)
                    i += 1
            temp = new_temp
            '''
            if j > k:
                t = temp[:]
                t[j], t[j-1] = t[j-1], t[j]     
                
                res.append(t)
                j -= 1
                i += 1
            else:
                temp = t
                k += 1
                j = n - 1
            '''
        return res
    '''
    def permute(self, nums):
        perms = [[]]   
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in xrange(len(perm)+1):   
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
            perms = new_perms
        return perms
    '''
    '''        
    # DFS
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)        
    '''
    '''
    public List<List<Integer>> permute(int[] nums) {
        ArrayList<List<Integer>> result = new ArrayList<List<Integer>>();
        helper(nums.length, result,new ArrayList<Integer>(), nums);
        return result;
    }
    public void helper(int len, ArrayList<List<Integer>> result, ArrayList<Integer> curr, int[] nums){
        for(int i=0; i<len;i++){
            if(!curr.contains(nums[i])) {//if curr already contains nums[i], skip
                curr.add(nums[i]); //add nums[i] if curr does not contain it
                if(curr.size() == len) result.add(new ArrayList<Integer>(curr)); //if curr is full(has size of the input array), put it into the result list
                else helper(len, result, curr, nums); //otherwise call self
                curr.remove(curr.size()-1); //backtracking
            }
        }
    }
    '''
        
ex46 = Ex46()
nums = [1,2,3,4]
print 46, ex46.permute(nums)

