class Ex45(object):    
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Slow
        if len(nums) == 1:
            return 0
        n = len(nums)
        B = [0] * n
        max = None
        i = 0
        last_sweep = [(nums[0], 0)]
        processed = set([0])
        while True:
            cur_sweep = []
            i += 1
            for m in range(len(last_sweep)):
                (v, j) = last_sweep[m]
                temp = nums[j]
                #for k in range(j+1, j+nums[j]+1):
                for k in range(j+nums[j], j, -1):
                    #print 71, i, j, k, last_sweep, cur_sweep
                    if k >= n - 1:
                        print 97, m, (v, j), len(last_sweep), last_sweep[-10:], n
                        return i
                    if k not in processed:
                        processed.add(k)
                        cur_sweep.append((nums[k], k))
            print 99, len(cur_sweep), cur_sweep[:10]
            cur_sweep.sort(reverse = True)
            last_sweep = cur_sweep
            print 102, len(cur_sweep), cur_sweep[:10]
            
    def jump0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        n = len(nums)        
        max = None
        i = 0
        last_sweep = [0]
        processed = set([0])
        while True:
            cur_sweep = []
            i += 1
            for j in last_sweep:
                temp = nums[j]
                for k in range(j+nums[j], j, -1):
                    #print 71, i, j, k, last_sweep, cur_sweep
                    if k == n - 1:
                        print 127, k, nums[k], len(last_sweep), last_sweep[-10:]
                        return i
                    if k not in processed:
                        processed.add(k)
                        cur_sweep.append(k)
            last_sweep = cur_sweep
    '''
    int jump(int A[], int n) {
         if(n<2)return 0;
         int level=0,currentMax=0,i=0,nextMax=0;

         while(currentMax-i+1>0){       //nodes count of current level>0
             level++;
             for(;i<=currentMax;i++){   //traverse current level , and update the max reach of next level
                nextMax=max(nextMax,A[i]+i);
                if(nextMax>=n-1)return level;   // if last element is in level+1,  then the min jump=level 
             }
             currentMax=nextMax;
         }
         return 0;
        }
    '''
    '''
    class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step
    '''
    
ex45 = Ex45()
nums = [2,2, 3,1,1,4]
print 45, ex45.jump(nums)

