class Ex216(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = range(1,10)
        target = n
        res = []
        self.backtrack(res, 0, candidates, [], target, 0, k)
        return res
        
    def backtrack(self, res, order, cand, path, left, start, k):
        if left == 0:
            if order == k:
                #return path
                res.append(path)
            return
        if left < 0:
            return
        for i in range(start, len(cand)):
            if i > start and cand[i] == cand[i - 1]:
                continue
            if cand[i] > left:
                continue
            temp = path[:]
            temp.append(cand[i])
            self.backtrack(res, order + 1, cand, temp, left - cand[i], i + 1, k)
            
        
    def combinationSum30(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = range(1,10)
        #print candidates
        target = n
        res = []
        output = []
        for i in candidates:
            #print 66, i, target
            if i > target:
                continue
            n = len(res)
            
            res.append([i])
            #print 66, res, n, i
            
            for j in range(n):
                #print 70, res[j], res
                temp = sum(res[j])
                if temp + i <= target:
                    res += [res[j][:]]
                    res[j].append(i)
                    #print 76, res, res[j]
                    
                #print 74, res[j], res, j        
        #print 75, res
        for cand in res:               
            if sum(cand) == target and len(cand) == k:
                cand.sort()
                if cand not in output:
                    output.append(cand)
        return output
    '''
    class Solution:
        # @param {integer} k
        # @param {integer} n
        # @return {integer[][]}
        def combinationSum3(self, k, n):
            if n > sum([i for i in range(1, 11)]):
                return []

            res = []
            self.sum_help(k, n, 1, [], res)
            return res


        def sum_help(self, k, n, curr, arr, res):
            if len(arr) == k:
                if sum(arr) == n:
                    res.append(list(arr))
                return

            if len(arr) > k or curr > 9:
                return
            
            for i in range(curr, 10):
                arr.append(i)
                self.sum_help(k, n, i + 1, arr, res)
                arr.pop()
    '''
    
ex216 = Ex216()
k = 3
n = 7
print 216, ex216.combinationSum3(k, n)

