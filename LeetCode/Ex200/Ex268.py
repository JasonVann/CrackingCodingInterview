class Ex268(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set()
        a_max = max(nums)
        if len(nums) == 0:
            a_max = 0
        for i in nums:
            a.add(i)
        for i in range(a_max):
            if i not in a:
                return i
        return a_max + 1
    
    def missingNumber0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Slow
        a = 0
        for i in nums:
            a += 1 << i
        a_max = max(nums)
        if len(nums) == 0:
            return 0
        str_a = str(bin(a))[2:]
        for i in range(1, len(str_a)):
            if str_a[-i] == 0:
                return i-1
        return a_max + 1    
    '''
    int missingNumber(vector<int>& nums) {
        long n = nums.size();
        return n * (n+1) / 2 - accumulate(begin(nums), end(nums), 0);
    }
    int missingNumber(vector<int>& nums) {
        int miss = 0, i = 0;
        for (int num : nums)
            miss += ++i - num;
        return miss;
    }
    public int missingNumber(int[] nums) { //xor
        int res = nums.length;
        for(int i=0; i<nums.length; i++){
            res ^= i;
            res ^= nums[i];
        }
        return res;
    }
    public int missingNumber(int[] nums) { //binary search
        Arrays.sort(nums);
        int left = 0, right = nums.length, mid= (left + right)/2;
        while(left<right){
            mid = (left + right)/2;
            if(nums[mid]>mid) right = mid;
            else left = mid+1;
        }
        return left;
    }
    '''

