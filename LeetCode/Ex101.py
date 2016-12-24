
class Ex101(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        level = 0
        queue = []
        queue.append([root])
                
        while len(queue) > 0:
            cur_level = queue[0]
            new_level = []
            #return cur_level
            for node in cur_level:
                #return node
                if node.left != None:
                    new_level.append(node.left)
                else:
                    new_level.append(root)
                if node.right != None:
                    new_level.append(node.right)
                else:
                    new_level.append(root)
            if len(new_level) > 1 and len(new_level) % 2 == 1:
                return False
            #return new_level
            for i in range(len(new_level)/2):
                if new_level[i].val != new_level[-i-1].val:
                    #return new_level
                    return False
            new_level = [a for a in new_level if a != root]
            queue.pop(0)
            if new_level != []:
                queue.append(new_level)            
        return True
