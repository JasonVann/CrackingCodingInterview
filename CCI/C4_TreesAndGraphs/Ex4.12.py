from tree import Tree_Node


def find_sum(root, target):
    def recur(node, lookup, depth, running_sum):
        running_sum += node.val
        if running_sum not in lookup:
            lookup[running_sum] = 1
        else:
            lookup[running_sum] += 1
        c1, c2 = 0, 0
        if node.left:
            c1 = recur(node.left, lookup, depth+1, running_sum)
        if node.right:
            c2 = recur(node.right, lookup, depth+1, running_sum)
        count = c1 + c2
        lookup[running_sum] -= 1
        if running_sum - target in lookup:
            count += lookup[running_sum - target]
        if running_sum == target:
            count += 1
        return count

    count = recur(root, {}, 0, 0)
    return count

def test():
    root = Tree_Node(10)
    n2 = Tree_Node(5)
    root.left = n2
    n3 = Tree_Node(-3)
    root.right = n3
    n4 = Tree_Node(3)
    n5 = Tree_Node(1)
    n2.left = n4
    n2.right = n5
    n6 = Tree_Node(11)
    n7 = Tree_Node(3)
    n3.right = n6
    n4.left = n7
    n8 = Tree_Node(-2)
    n4.right = n8
    n9 = Tree_Node(2)
    n5.right = n9
    #res = find_path(root, n6)
    res = find_sum(root, 11)
    return res


print(test())
