class Ex77(object):
    def bt(self, A, cur, n, start, left):
        if left == 0:
            A.append(cur[:])
            return
        if n - start == left:
            cur1 = cur[:]
            #print 60, range(start, n), start, cur
            cur1 += range(start, n)
            A.append(cur1)
            return
        self.bt(A, cur[:] + [start], n, start + 1, left - 1)        
        self.bt(A, cur[:], n, start + 1, left)
        return
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        A = []
        self.bt(A, [], n+1, 1, k)
        return A
    '''
    def combine(self, n, k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
    '''
    '''
    class Solution {
    public:
        vector<vector<int> > combine(int n, int k) {
            vector<vector<int> >res;
            if(n<k)return res;
            vector<int> temp(0,k);
            combine(res,temp,0,0,n,k);
            return res;
        }
        
        void combine(vector<vector<int> > &res,vector<int> &temp,int start,int num,int n ,int k){
            if(num==k){
                res.push_back(temp);
                return;
            }
            for(int i = start;i<n;i++){
                temp.push_back(i+1);
                combine(res,temp,i+1,num+1,n,k);
                temp.pop_back();
                }
            }
    };
    '''
    
     
ex77 = Ex77()
print 77, ex77.combine(4, 2)

