class Ex260(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        res = []
        for k, v in dic.items():
            if v == 1:
                res.append(k)
        return res
    '''
    public class Solution {
        public int[] singleNumber(int[] nums) {
            // Pass 1 : 
            // Get the XOR of the two numbers we need to find
            int diff = 0;
            for (int num : nums) {
                diff ^= num;
            }
            // Get its last set bit
            diff &= -diff;
            
            // Pass 2 :
            int[] rets = {0, 0}; // this array stores the two numbers we will return
            for (int num : nums)
            {
                if ((num & diff) == 0) // the bit is not set
                {
                    rets[0] ^= num;
                }
                else // the bit is set
                {
                    rets[1] ^= num;
                }
            }
            return rets;
        }
    }
    '''

