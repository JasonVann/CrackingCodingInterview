class Ex33(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        lr = nums[-1]
        rl = nums[0]
        n = len(nums)
        if n <= 2:
            if target not in nums:
                return -1
            return nums.index(target)
        
        l = 0
        r = n-1
        if nums[-1] > nums[0]:
            p = 0
        else:
            while l <= r:
                p = (l+r)/2
                print 78, p, nums[p], l, r
                if nums[p-1] > nums[p] and p == n - 1:
                    break
                if nums[p-1] > nums[p] < nums[p+1]:
                    break
                
                if nums[p] < nums[0]:
                    r = p - 1
                else:
                    l = p + 1
                print 81, l, r, p
        print 80, p
        if nums[p-1] < target or nums[p] > target:
            return -1
        
        if nums[-1] >= target:
            l = p
            r = n - 1
        else:
            l = 0
            r = p - 1
        print 91, l, r
        while l <= r:
            m = (l + r)/2
            print 99, m, nums[m], target
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            print 104, l, r, m
        return -1

    def search0(self, nums, target):
        if target not in nums:
            return -1
        return nums.index(target)
    '''
    class Solution {
    public:
        int search(int A[], int n, int target) {
            int lo=0,hi=n-1;
            // find the index of the smallest value using binary search.
            // Loop will terminate since mid < hi, and lo or hi will shrink by at least 1.
            // Proof by contradiction that mid < hi: if mid==hi, then lo==hi and loop would have been terminated.
            while(lo<hi){
                int mid=(lo+hi)/2;
                if(A[mid]>A[hi]) lo=mid+1;
                else hi=mid;
            }
            // lo==hi is the index of the smallest value and also the number of places rotated.
            int rot=lo;
            lo=0;hi=n-1;
            // The usual binary search and accounting for rotation.
            while(lo<=hi){
                int mid=(lo+hi)/2;
                int realmid=(mid+rot)%n; # !!
                if(A[realmid]==target)return realmid;
                if(A[realmid]<target)lo=mid+1;
                else hi=mid-1;
            }
            return -1;
        }
    };
    '''
    '''
    public class Solution {
        public int search(int[] A, int target) {
            int lo = 0;
            int hi = A.length - 1;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (A[mid] == target) return mid;
                
                if (A[lo] <= A[mid]) {
                    if (target >= A[lo] && target < A[mid]) {
                        hi = mid - 1;
                    } else {
                        lo = mid + 1;
                    }
                } else {
                    if (target > A[mid] && target <= A[hi]) {
                        lo = mid + 1;
                    } else {
                        hi = mid - 1;
                    }
                }
            }
            return A[lo] == target ? lo : -1;
        }
    }
    '''
    
ex33 = Ex33()
nums = [1,3,5]
target = 2

nums = [4, 5, 6, 7, 0, 1, 2]
target = 4
nums = [3,5,1]
target = 0
print 33, ex33.search(nums, target)

