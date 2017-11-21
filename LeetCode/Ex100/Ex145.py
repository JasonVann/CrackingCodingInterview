        
class Ex145(object):
    def postorderTraversal(self, root):
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
              
        self.recur(root.left, res)
        self.recur(root.right, res)        
        res.append(root.val) 
