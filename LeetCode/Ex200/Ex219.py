class Ex219(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            cur = nums[i]
            if cur in dic:
                dic[cur] += [i]
            else:
                dic[cur] = [i]
        for k in dic:
            v = dic[k]
            v.sort()
            for i in range(len(v)-1):
                if v[i] - v[i+1] <= -k:
                    return True
        return False
        
    def containsNearbyDuplicate0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            cur = nums[i]
            if cur in dic:
                for a in dic[cur]:
                    if abs(i-a) <= k:
                        return True
                dic[cur] += [i]
            else:
                dic[cur] = [i]
        return False
    '''
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(i > k) set.remove(nums[i-k-1]);
            if(!set.add(nums[i])) return true;
        }
        return false;
    }
    '''

