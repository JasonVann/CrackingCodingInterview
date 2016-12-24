class Ex228(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        l = None
        r = None
        cur = None
        last_end = None
        for i in nums:
            if l == None:
                l = i
                cur = i
            elif i == cur + 1:
                cur = i
            else:
                if l == cur:
                    res.append(str(l))
                else:
                    temp = str(l) + "->" + str(cur)
                    res.append(temp)
                last_end = cur
                l = i
                cur = i
        if l != None:
            if l == nums[-1]:
                res.append(str(l))
            else:
                temp = str(l) + "->" + str(nums[-1])
                res.append(temp)
        return res
    '''
    vector<string> summaryRanges(vector<int>& nums) {
        const int size_n = nums.size();
        vector<string> res;
        if ( 0 == size_n) return res;
        for (int i = 0; i < size_n;) {
            int start = i, end = i;
            while (end + 1 < size_n && nums[end+1] == nums[end] + 1) end++;
            if (end > start) res.push_back(to_string(nums[start]) + "->" + to_string(nums[end]));
            else res.push_back(to_string(nums[start]));
            i = end+1;
        }
        return res;
    }
    '''
    '''
    # !!
    def summaryRanges(self, nums):
        return [re.sub('->.*>', '->', '->'.join(`n` for i, n in g))
            for _, g in itertools.groupby(enumerate(nums), lambda (i, n): n-i)]
    '''
    '''
    def summaryRanges(self, nums):
        diff = [(n-i, n) for i, n in enumerate(nums)]
        first, last = dict(diff[::-1]), dict(diff)
        return [`n` + ('->'+`last[d]`)*(n<last[d]) for d, n in sorted(first.items())]
    '''
    '''
    def summaryRanges(self, nums):
        ranges, r = [], []
        for n in nums:
            if n-1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]
    '''

