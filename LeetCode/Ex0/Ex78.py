class Ex78(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]        
        #res = [[i] for i in nums]
        #print res
        for i in nums:
            temp = res[:]
            temp = [a+[i] for a in temp]
            res.extend(temp)
        #res = [[i] for i in nums]
        res += []
        #res += nums
        return res
    '''
    # DFS recursively 
    def subsets1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
        
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
            
    # Iteratively
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res
    '''
    '''
    public List<List<Integer>> subsets(int[] S) {
        Arrays.sort(S);
        int totalNumber = 1 << S.length;
        List<List<Integer>> collection = new ArrayList<List<Integer>>(totalNumber);
        for (int i=0; i<totalNumber; i++) {
            List<Integer> set = new LinkedList<Integer>();
            for (int j=0; j<S.length; j++) {
                if ((i & (1<<j)) != 0) {
                    set.add(S[j]);
                }
            }
            collection.add(set);
        }
        return collection;
    }
    '''
    
ex78 = Ex78()
nums = [1,2,3]
print 78, ex78.subsets(nums)

class Ex78(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res = [[i] for i in nums]
        return res
        
ex78 = Ex78()
nums = [1,2,3]
print 78, ex78.subsets(nums)
