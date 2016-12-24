class Ex179:
    # @param {integer[]} nums
    # @return {string}
    def compare(self, item1, item2):
        s1 = str(item1)
        s2 = str(item2)
        if len(s1) == len(s2):
            if item1 == item2:
                return 0
            if item1 < item2:
                return -1
            else:
                return 1
        if s1 + s2 > (s2 + s1):
            return 1
        elif s1 + s2 < s2 + s1:
            return -1
        return 0
        
    def largestNumber0(self, nums):
        dic = {}
        res = []
        for i in nums:
            digit0 = int(str(i)[0])
            if digit0 not in dic:
                dic[digit0] = [i]
            else:
                dic[digit0] += [i]
        keys = dic.keys()
        keys = dic.keys()
        if len(keys) == 0 or (len(keys) == 1 and 0 in keys):
            return "0"
        keys.sort(reverse = True)
        for k in keys:
            A = dic[k]
            #print 90, A
            A1 = sorted(A, cmp = self.compare, reverse = True)
            #A2 = sorted(A1, reverse=True)
            A2 = A1
            res += A2        
            #print 74, A, A1, A2
            
        res = [str(a) for a in res]
        print 98, res
        res = ''.join(res)
        #print 66, dic
        #print 89, res
        return res
                
    def largestNumber(self, nums):
        dic = {}
        res = []
        l = 0
        found = False
        for i in nums:
            if i > 0:
                found = True
        if not found:
            return "0"
        
        #A1 = sorted(A, key=lambda t: len(str(t)), reverse=False)
        #A1 = sorted(A, key=lambda t: (t[0], len(str(nums[t[1]]))), reverse=True)
        
        #A1 = sorted(A, key=lambda t: (len(str(nums[t[1]]))), reverse=False)
        #A1 = sorted(A, key=lambda t: (str(nums[t[1]])[1]), reverse=False)
        A1 = sorted(nums, cmp = self.compare, reverse=True)
        #A1 = sorted(A, reverse=True)
        print 74, A1
        res = [str(a) for a in A1]
        #print 121, res
        res = ''.join(res)
        return res
    '''
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x, y: cmp(y+x, x+y))
        return ''.join(num).lstrip('0') or '0'
    '''
    '''
    public class Solution {
        public String largestNumber(int[] num) {
            String[] array = Arrays.stream(num).mapToObj(String::valueOf).toArray(String[]::new);
            Arrays.sort(array, (String s1, String s2) -> (s2 + s1).compareTo(s1 + s2));
            return Arrays.stream(array).reduce((x, y) -> x.equals("0") ? y : x + y).get();
        }
    }
    '''
         
ex179 = Ex179()
nums = [2, 1, 3, 34, 30, 5, 9]
nums = [3, 30, 34, 5, 9, 2, 10, 1]
nums = [824,938,1399,5607,6973,5703,9609,4398,8247]
nums = [121,12]
print 179, ex179.largestNumber(nums)

