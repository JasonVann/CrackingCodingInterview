class Ex41(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        t = 1
        for i in nums:
            if i > 0:
                if t == i:
                    t += 1
        return t
        
    def firstMissingPositive0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Only works if there's no duplicate
        t_sum = 0
        min = None
        max = -1
        count_pos = 0
        for i in nums:
            if i > 0:
                if i > max:
                    max = i
                if min == None or i < min:
                    min = i
                t_sum += i
                count_pos += 1
        
        if count_pos == 0:
            return 1
        t2 = sum(range(min, max+1))
        if min == max:
            if min != 1:
                return 1
            else:
                return min + 1
        if t2 == t_sum:
            if min > 1:
                return 1
            return max + 1
        else:
            return t2 - t_sum
    '''
    class Solution
    {
    public:
        int firstMissingPositive(int A[], int n)
        {
            for(int i = 0; i < n; ++ i)
                while(A[i] > 0 && A[i] <= n && A[A[i] - 1] != A[i])
                    swap(A[i], A[A[i] - 1]);
            
            for(int i = 0; i < n; ++ i)
                if(A[i] != i + 1)
                    return i + 1;
            
            return n + 1;
        }
    }
    public class Solution {
        public int firstMissingPositive(int[] nums) {
            // nums[i] -> i+1
            int next;
            for (int i = 0 ; i < nums.length; i++) {
                int curr = nums[i];
                if (curr > 0 && curr != i+1 && curr <= nums.length) {
                    do {
                        next = nums[curr-1];
                        nums[curr-1] = curr;
                        curr = next;
                    } while (curr > 0 && curr <= nums.length && nums[curr-1] != curr);
                }
            }
            int j;
            for (j = 0; j < nums.length; j++) {
                if (nums[j] != j+1)
                    break;
            }
            return j+1;
        }
    }
    '''

