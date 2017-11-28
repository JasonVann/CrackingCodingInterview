from tree import Tree_Node

def validate_BST(root):
    def validate(node, lower, upper):
        if node is None:
            return True
        if node.left:
            if node.left.val > node.val or node.left.val < lower:
                return False
        if node.right:
            if node.right.val < node.val or node.right.val > upper:
                return False
        left = validate(node.left, float('-inf'), node.val)
        right = validate(node.right, node.val, float('inf'))
        return left & right
    if root is None:
        return True
    return validate(root, float('-inf'), float('inf'))

def test():
    root = Tree_Node(5)
    #root.left = Tree_Node(5)
    root.left = Tree_Node(2)
    root.right = Tree_Node(7)
    root.left.right = Tree_Node(11)
    root.right.left = Tree_Node(6)
    '''
    root.add(2)
    root.add(7)
    root.add(1)
    root.add(3)
    root.add(6)
    root.add(8)
    '''
    res = validate_BST(root)
    return res

print(test())
