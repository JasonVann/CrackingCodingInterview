class Ex334(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # backtracking, slow
        if len(nums) < 2:
            return False
        c1 = nums[0]
        i = 1
        count = 0
        res = [nums[0]]
        stack = []
        while i < len(nums):
            if res[-1] > nums[i]:
                if len(res) == 2 and res[0] < nums[i]:
                    res[1] = nums[i]
                else:                    
                    stack.append((res, i, next_item))
                    res = [nums[i]]
            elif res[-1] < nums[i]:
                res.append(nums[i])
            if len(res) == 3:
                return True
            i += 1
            if i == len(nums):
                if len(stack) > 0:
                    (res, i, next_item) = stack.pop()
                    while i < len(nums) and nums[i] == next_item:
                        i += 1
                    print 362, (res, i)
        return len(res) >= 3
    '''
    !!!
    public boolean increasingTriplet(int[] nums) {
            // start with two largest values, as soon as we find a number bigger than both, while both have been updated, return true.
            int small = Integer.MAX_VALUE, big = Integer.MAX_VALUE;
            for (int n : nums) {
                if (n <= small) { small = n; } // update small if n is smaller than both
                else if (n <= big) { big = n; } // update big only if greater than small but smaller than big
                else return true; // return if you find a number bigger than both
            }
            return false;
        }
    public boolean increasingTriplet(int[] nums) {
        if (nums.length < 1) return false;
        int min = nums[0], first = min, second = min;
        int index = 1;
        for (int i = 0; i < nums.length; i++) {
            if (index == 1) {
                if (nums[i] <= first) {
                    first = nums[i];
                    min = first;
                } else {
                    second = nums[i];
                    index++;
                }
            } else {
                if (nums[i] > second) return true;
                else if (nums[i] <= min) {
                    min = nums[i];
                } else {
                    first = min;
                    second = nums[i];
                }
            }
        }
        return false;
    }
    '''

