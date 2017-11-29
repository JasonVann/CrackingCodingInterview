from tree import Tree_Node


def link_successors(root, node):
    # O(n) time, O(n) space
    def recur(node):
        if node.left:
            recur(node.left)
        #return node
        res.append(node)

        if node.right:
            recur(node.right)

    res = []
    if node is None:
        return res
    recur(root)
    for i, r in enumerate(res):
        if r == node:
            if i < len(res)-1:
                return res[i+1]
    return None

pre = None
def link_successor(root, target):
    def find_min(node):
        res = None
        if node.left:
            res = find_min(node.left)
            return res
        return node

    def recur(node):
        global pre
        if node.val < target.val:
            pre = node
            recur(node.right)
        elif node.val == target.val:
            if node == target:
                if node.right:
                    pre = find_min(node.right)
                    return pre
                else:
                    return pre
            else:
                pre = node
                recur(node.left)
        else:
            pre = node
            recur(node.left)


    recur(root)
    if pre.val < target.val:
        return None
    return pre.val


def test():
    root = Tree_Node(5)
    b = Tree_Node(6)
    #root.add(2)
    root.right = b
    root.add(7)
    root.add(1)
    root.add(3)
    root.add(2.9)
    root.add(3.1)
    root.add(2.89)
    root.add(2.91)
    root.add(5.9)
    #root.add(8)

    res = link_successor(root, b)
    return res


print(test())
