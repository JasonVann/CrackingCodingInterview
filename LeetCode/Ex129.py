class Ex129(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.iter(root, res, [])
        all = 0
        for cur in res:
            temp = cur[0]
            for i in range(1, len(cur)):
                temp = temp*10 + cur[i]
            all += temp
        return all
        
    def iter(self, root, res, cur):
        if root == None:
            return
        if root.left == None and root.right == None:
            res.append(cur + [root.val])
                
        self.iter(root.left, res, cur + [root.val])
        self.iter(root.right, res, cur + [root.val])
        return 

