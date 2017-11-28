from stack import Stack

class SetOfStacks():
    def __init__(self, capacity):
        self.set = []
        self.capacity = capacity
        self.count = 0

    def push(self, val):
        if self.count == 0 or self.set[self.count-1].size == self.capacity:
            stack = Stack()
            stack.push(val)
            self.set.append(stack)
            self.count += 1
        else:
            stack = self.set[-1]
            stack.push(val)

    def pop(self):
        if self.count == 0:
            return None
        stack = self.set[self.count-1]
        val = stack.pop()
        if stack.is_empty():
            self.set.pop()
            self.count -= 1
        return val

    def pop_at(self, i):
        # Here we assume it's OK to leave non-last plates partially filled
        if self.count == 0:
            return None
        stack = self.set[i]
        val = stack.pop()
        if stack.is_empty():
            self.set.pop(i)
            self.count -= 1
        return val

def test():
    s = SetOfStacks(2)
    s.push(1)
    s.push(2)
    print(s.count)
    s.push(3)
    s.push(4)
    print(s.count)
    print(s.pop_at(0))
    print(s.pop_at(0))
    print(s.count)

test()
