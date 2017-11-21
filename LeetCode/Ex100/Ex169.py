# Ex169
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for k, v in dic.items():
            if v > len(nums) / 2:
                return k
