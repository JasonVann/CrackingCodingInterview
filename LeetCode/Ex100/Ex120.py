class Ex120(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle[-1]) == 0:
            return 0
        cur = [triangle[0][0]]
        for i in range(1, len(triangle)):
            n = len(triangle[i])
            row = triangle[i]
            prev = cur[:]            
            cur = [None] * n
            for j in range(n):                
                #print 57, prev, row, j, i
                if j > 0 and j < i:
                    cur[j] = min(prev[j-1], prev[j]) + row[j]
                elif j == 0:
                    cur[j] = prev[j] + row[j]
                else:
                    #print 74, cur, prev[j-1], row[j]
                    cur[j] = prev[j-1] + row[j]
                #print 75, prev, cur
        return min(cur)
    '''
    int minimumTotal(vector<vector<int> > &triangle) {
        int n = triangle.size();
        vector<int> minlen(triangle.back());
        for (int layer = n-2; layer >= 0; layer--) // For each layer
        {
            for (int i = 0; i <= layer; i++) // Check its every 'node'
            {
                // Find the lesser of its two children, and sum the current value in the triangle with it.
                minlen[i] = min(minlen[i], minlen[i+1]) + triangle[layer][i]; 
            }
        }
        return minlen[0];
    }
    '''
    '''
    public class Solution {
        public int minimumTotal(List<List<Integer>> triangle) {
            for(int i = triangle.size() - 2; i >= 0; i--)
                for(int j = 0; j <= i; j++)
                    triangle.get(i).set(j, triangle.get(i).get(j) + Math.min(triangle.get(i + 1).get(j), triangle.get(i + 1).get(j + 1)));
            return triangle.get(0).get(0);
        }
    }
    '''
    
ex120 = Ex120()
tri = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print 120, ex120.minimumTotal(tri)

