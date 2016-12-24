class Ex40(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #import copy
        res = []
        output = []
        for i in candidates:
            if i > target:
                continue
            n = len(res)
            #print 66, res, n, i
            
            res.append([i])
            for j in range(n):
                #print 70, res[j], res
                temp = sum(res[j])
                if temp + i <= target:
                    res += [res[j][:]]
                    res[j].append(i)
                    #print 76, res, res[j]
                    
                #print 74, res[j], res, j        
        print 75, res
        for cand in res:               
            if sum(cand) == target:
                cand.sort()
                if cand not in output:
                    output.append(cand)
        return output
    '''
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
       List<List<Integer>> list = new LinkedList<List<Integer>>();
       Arrays.sort(candidates);
       backtrack(list, new ArrayList<Integer>(), candidates, target, 0);
       return list;
    }

    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] cand, int remain, int start) {
       
       if(remain < 0) return; /** no solution */
       else if(remain == 0) list.add(new ArrayList<>(tempList));
       else{
          for (int i = start; i < cand.length; i++) {
             if(i > start && cand[i] == cand[i-1]) continue; /** skip duplicates */
             tempList.add(cand[i]);
             backtrack(list, tempList, cand, remain - cand[i], i+1);
             tempList.remove(tempList.size() - 1);
          }
       }
    }
    '''
        
ex40 = Ex40()
cand = [10, 1, 2, 7, 6, 1, 5]
t = 8
print 40, ex40.combinationSum2(cand, t)

