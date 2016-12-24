class Ex15(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        dic = {}
        res = {}
        for n in nums:
            if n in dic:
                dic[n] = dic[n] + 1
            else:
                dic[n] = 1
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                third = 0 - nums[i] - nums[j]
                if (third) in dic:
                    if ((third == nums[i] or third == nums[j]) and nums[i] != nums[j] and dic[third] > 1) or (third != nums[i] and third != nums[j]) or (third == nums[i] and third == nums[j] and dic[third] > 2):
                        #print 1221, nums[i], nums[j], third, dic[third]
                        temp = [nums[i], nums[j], third]
                        temp.sort()
                        res[tuple(temp)] = 1
        #print res
        res_l = []
        for k in res:
            res_l.append(list(k))
        return res_l
    '''
    # Array Implementation
    List<List<Integer>> res = new LinkedList<>(); 
    for (int i = 0; i < num.length-2; i++) {
        if (i == 0 || (i > 0 && num[i] != num[i-1])) {
            int lo = i+1, hi = num.length-1, sum = 0 - num[i];
            while (lo < hi) {
                if (num[lo] + num[hi] == sum) {
                    res.add(Arrays.asList(num[i], num[lo], num[hi]));
                    while (lo < hi && num[lo] == num[lo+1]) lo++;
                    while (lo < hi && num[hi] == num[hi-1]) hi--;
                    lo++; hi--;
                } else if (num[lo] + num[hi] < sum) {
                    // improve: skip duplicates
                    while (lo < hi && num[lo] == num[lo+1]) lo++;
                    lo++;
                } else {
                    // improve: skip duplicates
                    while (lo < hi && num[hi] == num[hi-1]) hi--;
                    hi--;
                }
            }
        }
    }
    return res;
    '''
    
ex15 = Ex15()
nums = [-1, 0, 1, 2, -1, -4]
nums = [-1,0,1,0]
print 15, ex15.threeSum(nums)
