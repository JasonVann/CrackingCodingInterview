class Ex114(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        from collections import deque
        stack = deque()
        if root == None:
            return 
            
        stack.appendleft(root)
        prev = None
        while len(stack) > 0:
            node = stack.popleft()
            if node.right != None:
                rnode = node.right
                stack.appendleft(rnode)
            if node.left != None:
                stack.appendleft(node.left)                
                node.left = None
            if prev != None:
                prev.right = node
            prev = node
            
    def flatten0(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        from collections import deque
        stack = deque()
        if root == None:
            return 
            
        stack.appendleft(root)
        prev = None
        while len(stack) > 0:
            has_linked = False
            node = stack.popleft()
            if node.right != None:
                rnode = node.right
                stack.appendleft(rnode)
            if node.left == None:
                if prev != None:
                    prev.right = node      
                    has_linked = True
            else:
                if not has_linked and prev != None:
                    prev.right = node
                node.right = node.left
                stack.appendleft(node.left)                
                node.left = None
            prev = node
    
    '''
    public void flatten(TreeNode root) {
        if (root == null) return;
        
        TreeNode left = root.left;
        TreeNode right = root.right;
        
        root.left = null;
        
        flatten(left);
        flatten(right);
        
        root.right = left;
        TreeNode cur = root;
        while (cur.right != null) cur = cur.right;
        cur.right = right;
    }
    private TreeNode prev = null;

    public void flatten(TreeNode root) {
        if (root == null)
            return;
        flatten(root.right);
        flatten(root.left);
        root.right = prev;
        root.left = null;
        prev = root;
    }

    '''

