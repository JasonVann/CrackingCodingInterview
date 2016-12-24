class Ex31(object):
    def sort(self, nums, j):
        l = len(nums)
        #j = i + 1
        while j < l:
            k = j
            found = False
            while k < l - 1:
                if nums[k] > nums[k+1]:
                    nums[k+1], nums[k] = nums[k], nums[k+1]
                    found = True
                k += 1
            if not found:
                break
        return
        
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # largest: descresing num
        incre = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                incre = False
                break
        if incre:
            #nums = nums[::-1]
            self.sort(nums, 0)
            return nums
        k = len(nums) - 1
        stack = [(nums[-1], k)]
        while True:
            i = k - 1
            for i in range(k - 1, -1, -1):
            #while i > -1:
                min1 = nums[k]
                cur = nums[i]
                #print 73, min1, cur
                if cur >= min1:
                    stack.append((cur, i))
                    for (val, j) in stack:
                        if val > cur:
                            k = j
                            min1 = val
                            break
                    #k = i
                    #continue
                if cur < min1:    
                    print 74, nums[i], nums[k], nums
                    nums[i], nums[k] = nums[k], nums[i]
                    print 75, nums[i+1:], k
                    self.sort(nums, i+1)
                    return nums
                #i -= 1
            k -= 1                
                    
    '''
    public class Solution {
        public void nextPermutation(int[] nums) {
          if(nums.length<=1){
              return;
          }
          
          int i= nums.length-1;
          
          for(;i>=1;i--){
             
             if(nums[i]>nums[i-1]){ //find first number which is smaller than it's after number
                 break;
             }
          }
          
          if(i!=0){
              swap(nums,i-1); //if the number exist,which means that the nums not like{5,4,3,2,1}
          }
          
          reverse(nums,i);    
        }
        
        private void swap(int[] a,int i){
            for(int j = a.length-1;j>i;j--){
                if(a[j]>a[i]){
                    int t = a[j];
                    a[j] = a[i];
                    a[i] = t;
                    break;
                }
            }
        }
        
        private void reverse(int[] a,int i){//reverse the number after the number we have found
            int first = i;
            int last = a.length-1;
            while(first<last){
                int t = a[first];
                a[first] = a[last];
                a[last] = t;
                first ++;
                last --;
            }
        }
        
    }
    '''
ex31 = Ex31()

nums = [3,4,2,1]
#nums = [1,2,3,4,5]
#nums = [4,3,2,1]

nums = [4,2,0,2,3,2,0]
#nums = [1,3,2]
nums = [5,4,7,5,3,2]
nums = [0,0,4,2,1,0]
print 31, ex31.nextPermutation(nums)

