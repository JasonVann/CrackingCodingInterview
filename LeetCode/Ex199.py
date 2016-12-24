class Ex199(object):        
    def rightSideView0(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
            
        queue = []
        queue.append([root])
        res = [root.val]
        while len(queue) > 0:
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
            if level != []:
                queue.append(level)
            queue.pop(0)
            if level0!= []:
                res.append(level0[-1])
        return res
    '''
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        rightView(root, result, 0);
        return result;
    }
    
    public void rightView(TreeNode curr, List<Integer> result, int currDepth){
        if(curr == null){
            return;
        }
        if(currDepth == result.size()){
            result.add(curr.val);
        }
        
        rightView(curr.right, result, currDepth + 1);
        rightView(curr.left, result, currDepth + 1);
        
    }
    '''
