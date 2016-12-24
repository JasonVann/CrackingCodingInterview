class Ex107(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
            
        queue = []
        queue.append([root])
        res = [[root.val]]
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
                res.append(level0)
        return res[::-1]
    '''
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        LinkedList<List<Integer>> list = new LinkedList<List<Integer>>();
        addLevel(list, 0, root);
        return list;
    }

    private void addLevel(LinkedList<List<Integer>> list, int level, TreeNode node) {
        if (node == null) return;
        if (list.size()-1 < level) list.addFirst(new LinkedList<Integer>());
        list.get(list.size()-1-level).add(node.val);
        addLevel(list, level+1, node.left);
        addLevel(list, level+1, node.right);
    }
    '''
