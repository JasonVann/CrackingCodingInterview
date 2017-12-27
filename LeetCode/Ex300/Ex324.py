class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        import math
        n = len(nums)
        self.merge_sort(nums, 0, n-1)
        mid = math.ceil(n/2)
        #return
        res = []
        res = nums[:]
        i = mid - 1
        j = n - 1
        k = 0
        while i >= 0 and j >= mid:
            nums[k] = res[i]
            k += 1
            nums[k] = res[j]
            i -= 1
            j -= 1
            k += 1

        if i >= 0:
            nums[k] = res[i]
        if j >= mid:
            nums[k] = res[j]

        nums = res

    def merge_sort(self, A, l, r):
        # [l, r]
        if l < r:
            mid = int((r + l)/2)
            self.merge_sort(A, l, mid)
            self.merge_sort(A, mid+1, r)
            self.merge(A, l, mid, r)

    def merge(self, A, l, mid, r):
        # Merge [l: r]
        A_left = A[l:mid+1][:]
        A_right = A[mid+1:r+1][:]
        A_left.append(float('inf'))
        A_right.append(float('inf'))
        i = 0
        j = 0
        k = l
        while k <= r:
            if A_left[i] < A_right[j]:
                A[k] = A_left[i]
                i += 1
            else:
                A[k] = A_right[j]
                j += 1
            k += 1
