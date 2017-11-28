from tree import Tree_Node


def validate_depth(node):
    if node is None:
        return True, -1
    res1, d1 = validate_depth(node.left)
    res2, d2 = validate_depth(node.right)
    if res1 & res2 & (abs(d1-d2) <= 1):
        return True, max(d1, d2) + 1
    return False, None


def test():
    root = Tree_Node(5)
    #root.left = Tree_Node(5)
    #root.left = Tree_Node(5)
    #root.right = Tree_Node(7)
    #root.left.left = Tree_Node(1)
    #root.right.left = Tree_Node(6)

    root.add(2)
    root.add(7)
    root.add(1)
    root.add(3)
    root.add(6)
    root.add(8)

    res = validate_depth(root)
    return res


print(test())
