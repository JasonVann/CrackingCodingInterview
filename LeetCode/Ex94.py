class Ex94(object):
    # 97%
    def inorderTraversal(self, root):
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
        if root.left == None:
            res.append(root.val)
        else:
            self.recur(root.left, res)
            res.append(root.val)
        self.recur(root.right, res)
    '''
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nodes;
        stack<TreeNode*> toVisit;
        TreeNode* curNode = root;
        while (curNode || !toVisit.empty()) {
            if (curNode) {
                toVisit.push(curNode);
                curNode = curNode -> left;
            }
            else {
                curNode = toVisit.top();
                toVisit.pop();
                nodes.push_back(curNode -> val);
                curNode = curNode -> right;
            }
        }
        return nodes;
    }
    '''
