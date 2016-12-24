class Ex220(object):        
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0:
            return False
            
        dic_k = {}
        dic_v = {}
        for i in range(len(nums)):
            cur = nums[i]
            #print 67, cur, i, dic_v
            if cur not in dic_v:
                dic_v[cur] = i
            else:
                #print 70, dic_v, i
                if abs(i - dic_v[cur]) <= k:
                    return True
                else:
                    dic_v[cur] = i
            if t == 0:
                continue
            to_remove = []
            for a, b in dic_v.items():
                if a == cur:
                    continue
                if b < i - k:
                    to_remove.append(a)
                    continue
                if abs(a - cur) <= t:
                    return True
            for a in to_remove:
                dic_v.pop(a)            
            
        return False
    '''
    # !!
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in xrange(n):
            m = nums[i] / w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] / w]
        return False
    '''
    '''
    public class Solution {
        public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
            if (nums == null || nums.length == 0 || k <= 0) {
                return false;
            }

            final TreeSet<Integer> values = new TreeSet<>();
            for (int ind = 0; ind < nums.length; ind++) {

                final Integer floor = values.floor(nums[ind] + t);
                final Integer ceil = values.ceiling(nums[ind] - t);
                if ((floor != null && floor >= nums[ind])
                        || (ceil != null && ceil <= nums[ind])) {
                    return true;
                }

                values.add(nums[ind]);
                if (ind >= k) {
                    values.remove(nums[ind - k]);
                }
            }

            return false;
        }
    }
    '''
    
ex220 = Ex220()
nums = [-1,-1]
k = 1
t = 0
print 220, ex220.containsNearbyAlmostDuplicate(nums, k, t)
            

