class Ex116:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # Built on level-order traversal
        if root == None:
            return 
            
        queue = []
        queue.append([root])
        res = [[root.val]]
        while len(queue) > 0:
            level = []
            temp = queue[0]
            level0 = []
            prev = None
            for node in temp:  
                #level0.append(node.val)
                if node.left != None:
                    level.append(node.left)
                    level0.append(node.left.val)
                    
                if node.right != None:
                    level.append(node.right)
                    level0.append(node.right.val)
                    
            if level != []:
                for i in range(0, len(level) - 1):
                    level[i].next = level[i+1]
                queue.append(level)
            queue.pop(0)
            if level0!= []:               
                res.append(level0)
        #return res
        
    def connect2(self, root):
        # Built on level-order traversal
        if root == None:
            return 
            
        queue = []
        queue.append([root])
        res = [[root.val]]
        while len(queue) > 0:
            level = []
            temp = queue[0]
            level0 = []
            prev = None
            for node in temp:  
                #level0.append(node.val)
                if node.left != None:
                    level.append(node.left)
                    level0.append(node.left)
                    if prev != None:
                        prev.next = node.left
                    
                    prev = node.left
                if node.right != None:
                    level.append(node.right)
                    level0.append(node.right)
                    if prev != None:
                        prev.next = node.right
                    prev = node.right
            if level != []:
                queue.append(level)
            queue.pop(0)
            if level0!= []:
                res.append(level0)
        #return res
    '''
    public void connect(TreeLinkNode root) {
        TreeLinkNode level_start=root;
        while(level_start!=null){
            TreeLinkNode cur=level_start;
            while(cur!=null){
                if(cur.left!=null) cur.left.next=cur.right;
                if(cur.right!=null && cur.next!=null) cur.right.next=cur.next.left;
                
                cur=cur.next;
            }
            level_start=level_start.left;
        }
    }
    '''
    '''
    public void connect(TreeLinkNode root) {
        if(root == null)
            return;
            
        if(root.left != null){
            root.left.next = root.right;
            if(root.next != null)
                root.right.next = root.next.left;
        }
        
        connect(root.left);
        connect(root.right);
    }
    '''
