from tree import Tree_Node
from queue import deque


def common_ancestor(root, x, y):
    # O(n) space, O(n) time
    px = find_path(root, x)
    py = find_path(root, y)
    if px is None or py is None:
        return None
    if len(px) < len(py):
        px, py = py, px
        x, y = y, x
    last = root
    for i, node in enumerate(py):
        if px[i] != py[i]:
            return last
        last = node
    return last


def find_path(root, x):
    queue = deque([[root]])
    while len(queue) > 0:
        path = queue.popleft()
        end = path.pop()
        if end == x:
            path.append(end)
            return list(path)
        if end.left:
            path2 = list(path)
            path2.append(end)
            path2.append(end.left)
            queue.append(path2)
        if end.right:
            path3 = list(path)
            path3.append(end)
            path3.append(end.right)
            queue.append(path3)
    return None


def test():
    root = Tree_Node(5)
    n2 = Tree_Node(2)
    root.left = n2
    n3 = Tree_Node(7)
    root.right = n3
    n4 = Tree_Node(1)
    n5 = Tree_Node(3)
    n2.left = n4
    n2.right = n5
    n6 = Tree_Node(6)
    n7 = Tree_Node(8)
    n3.left = n6
    n3.right = n7
    n8 = Tree_Node(1)
    #res = find_path(root, n6)
    res = common_ancestor(root, n5, n8)
    return res


print(test())
