class Ex287(object):             
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_i = 1
        max_i = len(nums) - 1
        
        while True:
            mid = (max_i + min_i) / 2
            l = max_i - mid + 1
            if min_i > max_i:
                return max_i
            for i in nums:
                if max_i >= i >= mid:
                    l -= 1
            #return min_i, max_i, l
            if min_i == max_i and l < 0:
                return min_i
                
            if l >= 0:
                max_i = mid - 1
            elif l < 0:
                min_i = mid + 1
            
    '''
    def findArrayDuplicate(array):
        assert len(array) > 0

        # The "tortoise and hare" step.  We start at the end of the array and try
        # to find an intersection point in the cycle.
        slow = len(array) - 1
        fast = len(array) - 1

        # Keep advancing 'slow' by one step and 'fast' by two steps until they
        # meet inside the loop.
        while True:
            slow = array[slow]
            fast = array[array[fast]]

            if slow == fast:
                break

        # Start up another pointer from the end of the array and march it forward
        # until it hits the pointer inside the array.
        finder = len(array) - 1
        while True:
            slow   = array[slow]
            finder = array[finder]

            # If the two hit, the intersection index is the duplicate element.
            if slow == finder:
                return slow
    '''
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n2)
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]
                    
    def findDuplicate0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a_set = set()
        for i in nums:
            if i in a_set:
                return i
            a_set.add(i)
        return -1
            
    def findSingle(self, nums):
        if len(nums) == 0:
            return 0
        res = nums[1]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res

