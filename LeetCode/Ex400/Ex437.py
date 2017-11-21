class Ex437(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.iter(root, sum, False, sum)
        
    def iter(self, root, sum, has_started, sum0):
        if root == None:
            return 0
        cur = 0
        #if root.left == None and root.right == None:
        if root.val == sum:
            cur = 1
            
        res1 = self.iter(root.left, sum - root.val, True, sum0)
        res2 = self.iter(root.right, sum - root.val, True, sum0)  
        res3, res4 = 0, 0
        if not has_started:
            res3 = self.iter(root.left, sum0, False, sum0)
            res4 = self.iter(root.right, sum0, False, sum0)
        #return 300 (res1, res2, res3, res4)
        return cur + res1 + res2 + res3 + res4
        
    '''
        def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        self.count = 0
        preDict = {0: 1}
        def dfs(p, target, pathSum, preDict):
            if p:
                pathSum += p.val
                self.count += preDict.get(pathSum - target, 0)
                preDict[pathSum] = preDict.get(pathSum, 0) + 1
                dfs(p.left, target, pathSum, preDict)
                dfs(p.right, target, pathSum, preDict)
                preDict[pathSum] -= 1
        dfs(root, target, 0, preDict)
        return self.count
    '''
    '''
    public class Solution {
        public int pathSum(TreeNode root, int sum) {
            if(root == null)
                return 0;
            return findPath(root, sum) + pathSum(root.left, sum) + pathSum(root.right, sum);
        }
        
        public int findPath(TreeNode root, int sum){
            int res = 0;
            if(root == null)
                return res;
            if(sum == root.val)
                res++;
            res += findPath(root.left, sum - root.val);
            res += findPath(root.right, sum - root.val);
            return res;
        }
       
    }
    '''

