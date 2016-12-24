class Ex337(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.val == None or (root.left == None and root.right == None):
            return root.val
        A = []
        #B = []
        last_level = []
        last_level.append((root, root.val))
        level = last_level[:]
        last_level_unchosen = [(root, 0)]
        level_alter = last_level[:]
        A.append(last_level)
        while len(last_level) > 0:            
            last_level = level
            last_level_alter = level_alter
            level = []
            level_alter = []
            for i in range(len(last_level)):
                (last_node, val) = last_level[i]
                (last_node_unchosen, val2) = last_level_unchosen[i]
                if last_node.left != None:
                    new_left = (last_node.left, val)
                    new_left2 = (last_node_unchosen.left, val2 + last_node_unchosen.left.val)
                    if new_left[1] > new_left2[1]:
                        level.append(new_left)
                    else:
                        level.append(new_left2)
                    level_alter.append(new_left)
                if last_node.right != None:
                    new_right = (last_node.right, val)
                    new_right2 = (last_node_unchosen.right, val2 + last_node_unchosen.right.val)
                    if new_right[1] > new_right2[1]:
                        level.append(new_right)
                    else:
                        level.append(new_right2)
                    level_alter.append(new_right)
            
            A.append(level)
            
    def rob0(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.val == None or (root.left == None and root.right == None):
            return root.val
        A = []
        last_level = []
        last_level.append((root, root.val))
        level = last_level[:]
        last_level_unchosen = [(root, 0)]
        A.append(last_level)
        while len(last_level) > 0:            
            last_level = level
            level = []
            for i in range(len(last_level)):
                (last_node, val) = last_level[i]
                (last_node_unchosen, val2) = last_level_unchosen[i]
                if last_node.left != None:
                    new_left = (last_node.left, val)
                    new_left2 = (last_node_unchosen.left, val2 + last_node_unchosen.left.val)
                    if new_left[1] > new_left2[1]:
                        level.append(new_left)
                    else:
                        level.append(new_left2)
                if last_node.right != None:
                    new_right = (last_node.right, val)
                    new_right2 = (last_node_unchosen.right, val2 + last_node_unchosen.right.val)
                    if new_right[1] > new_right2[1]:
                        level.append(new_right)
                    else:
                        level.append(new_right2)
            
            A.append(level)

