from stack import Stack

class Queue():
    def __init__(self):
        self.i = Stack()
        self.o = Stack()

    def push(self, val):
        self.i.push(val)

    def pop(self):
        if not self.o.is_empty():
            data = self.o.pop()
            return data
        while not self.i.is_empty():
            data = self.i.pop()
            self.o.push(data)
        if self.o:
            return self.o.pop()
        return None

    def peek(self):
        if not self.o.is_empty():
            data = self.o.peek()
            return data
        while not self.i.is_empty():
            data = self.i.pop()
            self.o.push(data)
        if self.o:
            return self.o.peek()
        return None

    def is_empty(self):
        if self.i.is_empty() and self.o.is_empty():
            return True
        return False

def test():
    q = Queue()
    print(q.peek())
    print(q.is_empty())
    q.pop()
    q.push(1)
    print(q.peek())
    print(q.is_empty())
    q.push(2)
    q.push(3)
    print(q.peek())
    print(q.pop())
    print(q.pop())
    print(q.peek())
    print(q.pop())
    print(q.is_empty())

test()
