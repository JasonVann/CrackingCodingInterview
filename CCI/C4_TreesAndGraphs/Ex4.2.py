from tree import Tree_Node

def build_minimal_tree(A):
    # A is sorted
    l = 0
    r = len(A)
    if r == 0:
        return Tree_Node(None)
    return insert(None, A, l, r-1)

def insert(tree, A, l, r):
    if l > r:
        return
    mid = (l+r)//2
    if tree is None:
        tree = Tree_Node(A[mid])
        #A[mid] = None
    else:
        tree.add(A[mid])
        #A[mid] = None
    left = insert(tree.left, A, l, mid-1)
    right = insert(tree.right, A, mid+1, r)
    tree.left = left
    tree.right = right
    return tree

def test():
    A = [1,2,3,5,6,7,8]
    tree = build_minimal_tree(A)
    tree.in_order()

test()
