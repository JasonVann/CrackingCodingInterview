class Ex350(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1, d2 = {}, {}
        res = []
        for a in nums1:
            d1[a] = d1.get(a, 0) + 1
        for a in nums2:
            if a in d1:
                res.append(a)
                d1[a] = d1.get(a,0) - 1
                if d1[a] <= 0:
                    d1.pop(a)
        return res
