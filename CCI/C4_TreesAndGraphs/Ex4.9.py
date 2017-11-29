from tree import Tree_Node

def sequence(node):
    def recur(node, path):
        if node.left is None and node.right is None:
            return [[node.val]]
        if node.left:
            left = recur(node.left, path)
            l = []
            for a in left:
                a.insert(0, node.val)
                l.append(a)

        if node.right:
            r = recur(node.right, path)
        # Then merge l, r
        res = []
        for i in l:
            for j in r:
                temp = merge(i, j)
                res += temp
        return res
    res = recur(node, [])
    return res

def merge(l, r):
    # Merge two lists, only keep orders within sublist
    temp = list(l)
    res = [(l[:], -1)]
    for item in r:
        res2 = []
        for temp, index in res:
            for j in range(index + 1, len(temp)+1):
                temp2 = temp[:]
                temp2.insert(j, item)
                res2.append((temp2, j))
        res = res2
    ans = []
    for item, path in res:
        ans.append(item)
    return ans

def test():
    root = Tree_Node(5)
    #b = Tree_Node(2)
    root.add(2)
    #root.right = b
    root.add(7)
    root.add(1)
    root.add(3)
    res = sequence(root)
    print(res)

def test2():
    l = [2, 3]
    r = [7, 6]
    res = merge(l, r)
    print(res)

test()
test2()