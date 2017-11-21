class Ex414(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in range(3):
            cur_max = max(nums)
            nums = [e for e in nums if e != cur_max]
            res += [cur_max]
            if nums == [] and i < 2:
                return max(res)
        return cur_max

