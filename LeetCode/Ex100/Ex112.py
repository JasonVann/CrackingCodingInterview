class Ex112(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.left == None and root.right == None:
            if root.val == sum:
                return True
            else:
                return False
        res1 = self.hasPathSum(root.left, sum - root.val)
        res2 = self.hasPathSum(root.right, sum - root.val)
        return res1 | res2
