# Ex1
class Solution(object):
    def twoSum(self, nums, target):
        i = 0 
        # is_asc = False
        # if nums[0] > nums[1]:
            # is_asc = True
        while i < len(nums):
            j = i + 1
            temp = target - nums[i]
            while j < len(nums):
                if temp == nums[j]:
                    return [i, j]
                # if temp < 0 and is_asc:
                    # # nums are pre-sorted
                    # break
                # if temp > 0 and not is_asc:
                    # break
                j += 1
            i += 1
        return []

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i+1]
            else:
                buff_dict[target - nums[i]] = i+1
