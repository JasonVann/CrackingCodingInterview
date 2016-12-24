
class Ex110(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        (level, ans) = self.helper(root, 1)
        return ans
        
    def helper(self, root, level):
        if root == None:
            return (level-1, True)
        else:
            (l, lb) = self.helper(root.left, level+1)
            (r, rb) = self.helper(root.right, level+1)
            if lb == False or rb == False:
                return (max(l, r), False)
            if abs(l - r) > 1:
                return (max(l, r), False)
            return (max(l,r), True)
            
    '''
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def depth(node):
            if not node:    #leaves
                return 0
            left = depth(node.left) #left child's depth
            right = depth(node.right) #right child's depth
            if abs(left-right)>1:
                raise Exception #stop recursion and report unbalance
            return max(left, right)+1
        try:
            return abs(depth(root.left)-depth(root.right))<=1
        except:
            return False
    '''
    '''
    public boolean isBalanced(TreeNode root) {
        if(root==null){
            return true;
        }
        return height(root)!=-1;
        
    }
    public int height(TreeNode node){
        if(node==null){
            return 0;
        }
        int lH=height(node.left);
        if(lH==-1){
            return -1;
        }
        int rH=height(node.right);
        if(rH==-1){
            return -1;
        }
        if(lH-rH<-1 || lH-rH>1){
            return -1;
        }
        return Math.max(lH,rH)+1;
    }
    '''
