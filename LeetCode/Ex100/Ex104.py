class Ex104(object):
    def maxDepth(self, root):
        return self.helper(root, 1)
        
    def helper(self, root, level):
        if root == None:
            return level-1
        else:
            l = self.helper(root.left, level+1)
            r = self.helper(root.right, level+1)
            return max(l, r)
    '''
    public int maxDepth(TreeNode root) {
        if(root==null){
            return 0;
        }
        return 1+Math.max(maxDepth(root.left),maxDepth(root.right));
    }
    '''
    def maxDepth0(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        # Faster
        depth = 0
        max_depth = 0
        if root == None:
            return depth
            
        queue = []
        queue.append([root])
        res = [[root.val]]
        while len(queue) > 0:
            depth += 1
            level = []
            temp = queue[0]
            level0 = []
            for node in temp:  
                #level0.append(node.val)
                if node.left != None:
                    level.append(node.left)
                    level0.append(node.left.val)
                if node.right != None:
                    level.append(node.right)
                    level0.append(node.right.val)
                else:
                    if node.left == None:
                        if depth > max_depth:
                            max_depth = depth
            if level != []:
                queue.append(level)
            queue.pop(0)
            if level0!= []:
                res.insert(0, level0)            
            
        return max_depth
