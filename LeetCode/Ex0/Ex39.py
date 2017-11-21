class Ex39(object):
    def combinationSum1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        last = res
        candidates.sort()
        while True:
            last = res
            for i in range(len(candidates)):
                cur = candidates[i]
                if cur <= target:
                    back = res
                    res = [a + [cur] for a in res if sum(a) + cur <= target]
                    res += back
                    #print 64, res
                    res.append([cur])
                    #print 66, res, cur
            
            '''
            # Method1 to de-duplicate: use set
            res = [tuple(sorted(a)) for a in res]
            #print 72, res
            res = set(res)
            #print 76, res
            res = [list(a) for a in res]
            res = list(res)
            #res.sort()
            
            # Method2: use loop
            res = [sorted(a) for a in res]
            res2 = []
            for a in res:
                if a not in res2:
                    res2.append(a)
            
            l_res = 0
            for a in res:
                l_res += len(a)
            #print 80, last
            #print 81, res
            if l_last == l_res:
                break
            
            res = res2
            if last == res:
                break
            '''
        res = filter(lambda x: sum(x) == target, res)
        return res
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 10 times faster
        res = []
        last = res        
        for i in range(len(candidates)):
            cur = candidates[i]
            if cur <= target:                    
                (a, b) = divmod(target, cur)
                if a > 0:
                    for j in range(1, a+1):      
                        back = res
                        #print 110, res
                        res = [e + j*[cur] for e in res if sum(e) + j*cur <= target]
                        #print 113, res
                        res.append(j*[cur])
                        res += back                   
            
        #print 150, res
        res = [tuple(sorted(a)) for a in res]
        res = set(res)        
        res = filter(lambda x: sum(x) == target, res)
        return res
    '''
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in xrange(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
    '''
    '''
    def combinationSum(self, candidates, target):
        candidates.sort()
        dp = [[[]]] + [[] for i in xrange(target)]
        for i in xrange(1, target + 1):
            for number in candidates:
                if number > i: break
                for L in dp[i - number]:
                    if not L or number >= L[-1]: dp[i] += L + [number],
        return dp[target]
    '''
    
ex39 = Ex39()

nums = [2,3,6,7]
target = 7

nums = [2,5,8,4]
target = 10
nums = [8,7,3,11,4,12]
target = 26
nums = [26,40,35,41,49,39,47,20,38,44,32,43,37,36,42,25,33,30,24,29,45,22,28,48,23]
target = 64
nums = [2,1]
target = 3
print 39, ex39.combinationSum(nums, target)
print time.time() - start_time
