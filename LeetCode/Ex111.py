class Ex111(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        #64ms, 92%
        depth = 0
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
                        return depth
            if level != []:
                queue.append(level)
            queue.pop(0)
            if level0!= []:
                res.insert(0, level0)            
            
        return depth
    '''
    public static int minDepth(TreeNode root) {
        if (root == null)   return 0;
        if (root.left == null)  return minDepth(root.right) + 1;
        if (root.right == null) return minDepth(root.left) + 1;
        return Math.min(minDepth(root.left),minDepth(root.right)) + 1;
    }
    '''
