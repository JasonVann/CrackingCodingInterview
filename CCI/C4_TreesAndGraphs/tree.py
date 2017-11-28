class Tree_Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add(self, val):
        if val <= self.val:
            if self.left:
                self.left.add(val)
            else:
                self.left = Tree_Node(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = Tree_Node(val)

    def pre_order(self):
        print(self.val)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.val)
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.val)


def test():
    tree = Tree_Node(5)
    tree.add(7)
    tree.add(2)
    tree.add(8)
    tree.add(6)
    tree.add(1)
    tree.add(3)
    #tree.pre_order()
    #tree.in_order()
    tree.post_order()

test()
