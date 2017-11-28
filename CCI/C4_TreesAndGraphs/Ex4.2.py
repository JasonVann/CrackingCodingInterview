from tree import Tree_Node

def build_minimal_tree(A):
    # A is sorted
    l = 0
    r = len(A)
    if r == 0:
        return Tree_Node(None)
    return insert(None, A, l, r)

def insert(tree, A, l, r):
    if l >= r:
        return
    mid = (l+r)//2
    if tree is None:
        tree = Tree_Node(A[mid])
        A[mid] = None
    else:
        if A[mid] is None:
            return
        tree.add(A[mid])
        A[mid] = None
    insert(tree, A, l, mid)
    insert(tree, A, mid, r)
    return tree

def test():
    A = [1,2,3,5,6,7,8]
    tree = build_minimal_tree(A)
    tree.in_order()

test()
