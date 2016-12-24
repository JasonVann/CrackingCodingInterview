class Ex98(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recur(root, None, None)
        
    def recur(self, root, min_v, max_v):
        res = True
        if root == None:
            return True
        res_l = True
        res_r = True
        
        if root.left != None:
            if root.left.left == None and root.left.right == None:
                if min_v != None:
                    res1 = min_v < root.left.val < root.val
                else:
                    res1 = True
                if max_v != None:
                    res2 = max_v > root.val > root.left.val
                else:
                    res2 = True
                res_l = res1 & res2 & (root.left.val < root.val)
            else:
                res1 = self.recur(root.left.left, min_v, root.left.val)
                res2 = self.recur(root.left.right, root.left.val, root.val)
                if max_v != None:
                    res3 = (max_v > root.val > root.left.val)
                else:
                    res3 = root.val > root.left.val
                if min_v != None:
                    res4 = (root.val > root.left.val > min_v)
                else:
                    res4 = root.val > root.left.val
                res_l = res1 & res2  & res3 & res4
        else:
            res_l = True
            
        if root.right != None:
            if root.right.left == None and root.right.right == None:
                if min_v != None:
                    res1 = min_v < root.val < root.right.val
                else:
                    res1 = True
                if max_v != None:
                    res2 = max_v > root.right.val > root.val
                else:
                    res2 = True                    
                res_r = res1 & res2 & (root.right.val > root.val)
            else:
                res1 = self.recur(root.right.left, root.val, root.right.val)
                res2 = self.recur(root.right.right, root.val, max_v)
                if max_v != None:
                    res3 = (max_v > root.right.val > root.val)
                else:
                    res3 = root.right.val > root.val
                if min_v != None:
                    res4 = (root.right.val > root.val > min_v)
                else:
                    res4 = root.right.val > root.val  
                #return res2, root.val, root.right.val, min_v, max_v
                res_r = res1 & res2 & res3 & res4
        else:
            res_r = True
            
        # Then check root
        if min_v != None:
            res1 = min_v < root.val
        else:
            res1 = True
        if max_v != None:
            res2 = max_v > root.val
        else:
            res2 = True
        
        return res1 & res2 & res_l & res_r
    '''
    class Solution {
    public:
        bool isValidBST(TreeNode* root) {
            TreeNode* prev = NULL;
            return validate(root, prev);
        }
        bool validate(TreeNode* node, TreeNode* &prev) {
            if (node == NULL) return true;
            if (!validate(node->left, prev)) return false;
            if (prev != NULL && prev->val >= node->val) return false;
            prev = node;
            return validate(node->right, prev);
        }
    };
    '''
