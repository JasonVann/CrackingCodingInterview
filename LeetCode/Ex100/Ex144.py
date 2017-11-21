class Ex144(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.recur(root, res)
        return res
        
    def recur(self, root, res):
        if root == None:
            return 
        
        res.append(root.val)        
        self.recur(root.left, res)
        self.recur(root.right, res)
