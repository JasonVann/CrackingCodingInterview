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
                # Can be changed to handle duplicate
                return False
        left = validate(node.left, float('-inf'), node.val)
        right = validate(node.right, node.val, float('inf'))
        return left & right
    if root is None:
        return True
    return validate(root, float('-inf'), float('inf'))


last_printed = None


def validate_BST2(node):
    # CCI Sol
    # Cannot handle duplicates
    global last_printed
    if node == None:
        return True
    if not validate_BST2(node.left):
        return False
    if last_printed is not None and last_printed >= node.val:
        return False
    last_printed = node.val
    if not validate_BST2(node.right):
        return False
    return True


def test():
    root = Tree_Node(5)
    #root.left = Tree_Node(5)
    root.left = Tree_Node(5)
    root.right = Tree_Node(7)
    root.left.left = Tree_Node(1)
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
    print(last_printed)
    return res


print(test())
