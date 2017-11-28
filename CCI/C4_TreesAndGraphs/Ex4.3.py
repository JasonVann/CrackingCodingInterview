from tree import Tree_Node


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


def list_depth(root):
    from queue import Queue
    res = []
    queue = Queue()
    queue.put(root)
    tail = None
    head = None
    this_level = 1
    next_level = 0
    while not queue.empty():
        node = queue.get()
        if head is None:
            head = Node(node.val)
            tail = head
        else:
            tail.next = Node(node.val)
            tail = tail.next
        this_level -= 1
        if node.left:
            queue.put(node.left)
            next_level += 1
        if node.right:
            queue.put(node.right)
            next_level += 1
        if this_level == 0:
            res.append(head)
            head = None
            tail = None
            this_level = next_level
            next_level = 0

    return res


def test():
    root = Tree_Node(5)
    root.add(2)
    root.add(7)
    root.add(1)
    root.add(3)
    root.add(6)
    root.add(8)
    res = list_depth(root)
    return res
    
test()
