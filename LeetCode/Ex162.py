class Ex162(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n >= 2 and nums[0] > nums[1]:
            return 0
            
        for i in range(1, n-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i
        return n - 1
    '''
    # !!
    Invariant: nums[left - 1] < nums[left] && nums[right] > nums[right + 1]
    If num[i-1] < num[i] > num[i+1], then num[i] is peak
    If num[i-1] < num[i] < num[i+1], then num[i+1...n-1] must contains a peak
    If num[i-1] > num[i] > num[i+1], then num[0...i-1] must contains a peak
    If num[i-1] > num[i] < num[i+1], then both sides have peak
    class Solution {
    public:
        int findPeakElement(const vector<int> &num) 
        {
            int low = 0;
            int high = num.size()-1;
            
            while(low < high)
            {
                int mid1 = (low+high)/2;
                int mid2 = mid1+1;
                if(num[mid1] < num[mid2])
                    low = mid2;
                else
                    high = mid1;
            }
            return low;
        }
    };
    '''

