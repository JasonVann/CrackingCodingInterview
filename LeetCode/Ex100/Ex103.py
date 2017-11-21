class Ex103(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
            
        queue = []
        queue.append([root])
        res = [[root.val]]
        is_rev = True
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
                if is_rev:
                    level0.reverse() 
                is_rev = not is_rev                    
                res.append(level0)
        return res
