class Ex167(object):
    def twoSum(self, numbers, target):
        # O(n)
        dic = {}
        for i in range(len(numbers) - 1):
            cur = numbers[i]
            if cur not in dic:
                dic[cur] = [i]
            else:
                dic[cur].append(i)
            alt = target - cur
            if alt in dic:
                if alt == cur and len(dic[alt]) == 1:
                    continue
                j = dic[alt][0]
                return [j+1, i+1]
            
    def twoSum0(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(nlogn)
        p1 = 0
        p2 = 0
        n = len(numbers)
        while p1 < n:
            t = target - numbers[p1]
            l = p1 + 1
            r = n - 1
            while True:
                
                if l > r:
                    break
                
                mid = (l+r)/2
                #print 72, numbers[p1], numbers[mid], t, l, r, p1, mid
                if numbers[mid] > t:
                    r = mid - 1
                elif numbers[mid] == t:
                    return [p1+1,mid+1]
                else:
                    l = mid + 1
            p1 += 1
            
        return [p1+1, p2+1]
    '''
    # !!!
    public int[] twoSum(int[] num, int target) {
        int[] indice = new int[2];
        if (num == null || num.length < 2) return indice;
        int left = 0, right = num.length - 1;
        while (left < right) {
            int v = num[left] + num[right];
            if (v == target) {
                indice[0] = left + 1;
                indice[1] = right + 1;
                break;
            } else if (v > target) {
                right --;
            } else {
                left ++;
            }
        }
        return indice;
    }
    '''
    
ex167 = Ex167()
numbers = [2,3,4]
t = 6
print 167, ex167.twoSum(numbers, t)

