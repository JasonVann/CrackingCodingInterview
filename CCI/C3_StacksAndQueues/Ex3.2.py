class Stack():
    class Node():
        def __init__(self, val):
            self.val = val
            self.next = None
            self.min = None

    def __init__(self):
        self.top = None

    def push(self, val):
        node = self.Node(val)
        node.next = self.top # !!
        if self.top:
            if node.val < self.top.min:
                node.min = node.val
            else:
                node.min = self.top.min
        else:
            node.min = node.val
        self.top = node

    def peek(self):
        if self.top:
            return self.top.val
        else:
            return None

    def min(self):
        return self.top.min

    def pop(self):
        if self.top:
            data = self.top.val
            self.top = self.top.next
        else:
            data = None
        return data

    def is_empty(self):
        return self.top is None

def test():
    s = Stack()
    s.push(4)
    s.push(3)
    print(s.peek())
    print(s.min())

    s.push(2)
    s.push(1)
    print(s.pop())
    print(s.min())
    print(s.is_empty())

test()
