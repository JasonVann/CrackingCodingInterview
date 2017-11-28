class Stack():
    class Node():
        def init(self, val):
            self.val = val
            self.next = None

    def init(self):
        self.top = None

    def push(self, val):
        node = Node(val)
        node.next = self.top # !!
        self.top = node

    def peek(self):
        if self.top:
            return self.top.val
        else:
            return None

    def pop(self):
        if self.top:
            data = self.top.val
            self.top = self.top.next
        else:
            data = None
        return data
