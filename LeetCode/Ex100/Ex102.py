# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Ex102(object):
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
        return res
    '''
    def levelOrder(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ans
    '''
    
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
