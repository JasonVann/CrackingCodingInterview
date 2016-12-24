class Ex88(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        i = m - 1
        j = n - 1
        while j >= 0 and i >= 0:
            #print i, j, k
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else :
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        
        #print 'b', nums1, i, j, k
        if k >= 0 and j >= 0:
            nums1[:k+1] = nums2[:j+1]
        return nums1

ex88 = Ex88()
nums1=[2,0]
nums2=[1]
print 88, ex88.merge(nums1, 1, nums2, 1)
