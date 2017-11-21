class Ex113(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # 95%
        res = []
        self.iter(root, sum, res, [])
        return res
        
    def iter(self, root, sum, res, cur):
        if root == None:
            return
        if root.left == None and root.right == None:
            if root.val == sum:
                res.append(cur + [root.val])
                return 
            else:
                return
        self.iter(root.left, sum - root.val, res, cur + [root.val])
        self.iter(root.right, sum - root.val, res, cur + [root.val])
        return 

