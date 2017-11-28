class Queue():
    class Node():
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None

    def push(self, val):
        node = Node(val)
        if self.last:
            self.last.next = node
            self.last = self.last.next
        else:
            self.last = node
        if not self.first:
            self.first = node

    def peek(self):
        if self.first:
            return self.first.val
        else:
            return None

    def pop(self):
        if not self.first:
            return None
        data = self.first.val
        self.first = self.first.next
        if self.first is None: # !!
            self.last = None
        return data

    def is_empty(self):
        return self.first is None
