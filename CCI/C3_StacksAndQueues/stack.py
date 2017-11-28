class Stack():
    # By LinkedList
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

    def is_empty(self):
        return self.top is None


class Stack_array():
    def init(self):
        self.data = []
        self.size = 0

    def push(self, val):
        self.data.append(val)
        self.size += 1

    def pop(self, val):
        if self.size == 0:
            return None
        self.size -= 1
        item = self.data[self.size]

    def peek(self, val):
        if self.size == 0:
            return None
        return self.data[self.size-1]

    def is_empty(self):
        return self.size == 0
