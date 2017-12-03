class CircularArray():
    def __init__(self, capacity):
        self.data = [None]*capacity
        self.head = 0
        self.size = 0
        self.capacity = capacity
        self.current = -1

    def rotate(self, index):
        self.head = index
        self.current = -1

    def get(self, i):
        i = (i+self.head) % self.capacity
        return self.data[i]

    def set(self, i, val):
        i = (i+self.head) % self.capacity
        self.data[i] = val

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current >= self.capacity:
            self.current = -1
            raise StopIteration
        print(29, self.current)
        return self.get(self.current)

def test():
    ca = CircularArray(5)
    ca.set(0,1)
    ca.set(1,2)
    ca.set(2,3)
    ca.set(3,4)
    ca.set(4,5)
    print(ca.data)
    for a in ca:
        print(a)
    print('rotate')
    ca.rotate(2)
    print(ca.get(0))
    for a in ca:
        print(a)
    print(ca.current)

if __name__ == '__main__':
    test()
