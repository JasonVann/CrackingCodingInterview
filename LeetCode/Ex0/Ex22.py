class Ex22(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        if n <= 0:
            return res
        res.append((1, '('))
        for i in range(2*n):
            bak = res[:]
            res = [(a-1, b+')') for (a,b) in bak if len(b) < 2*n and a > 0]
            new2 = [(a+1, b+'(') for (a, b) in bak if (a+len(b)) < (2*n) and a < n]
            new3 = [(a, b) for (a, b) in bak if len(b) == 2*n]
            res = res + new2 + new3
            
        #print 113, res
        res2 = []
        for (a, b) in res:
            res2.append(b)
        return res2
        
    '''
    class Solution {
    public:
        vector<string> generateParenthesis(int n) {
            vector<string> res;
            addingpar(res, "", n, 0);
            return res;
        }
        void addingpar(vector<string> &v, string str, int n, int m){
            if(n==0 && m==0) {
                v.push_back(str);
                return;
            }
            if(m > 0){ addingpar(v, str+")", n, m-1); }
            if(n > 0){ addingpar(v, str+"(", n-1, m+1); }
        }
    };
    '''
ex22 = Ex22()
print 22, ex22.generateParenthesis(3)
