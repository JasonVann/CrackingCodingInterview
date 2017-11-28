class Min_Heap():
    def __init__(self):
        self.data = []
        self.size = 0

    def insert(self, val):
        # Bubble up
        self.data.append(val)
        index = self.size
        self.size += 1
        while index > 1 and val < self.data[self.parent(index)]:
            self.data[index], self.data[self.parent(index)] = self.data[self.parent(index)], self.data[index]
            index = self.parent(index)

    def extract_min(self):
        min_val = self.data[0]
        self.data[0] = self.data[self.size-1]
        self.data.pop(-1)
        self.size -= 1
        index = 0
        while True:
            if 2*index + 1< self.size and self.data[index] > self.data[2*index+1]:
                self.data[2*index+1], self.data[index] = self.data[index], self.data[2*index+1]
            elif 2*index + 2 < self.size and self.data[index] > self.data[2*index+2]:
                self.data[2*index+2], self.data[index] = self.data[index], self.data[2*index+2]
            else:
                break
            index = index*2
        return min_val

    def parent(self, index):
        return index//2-1


def test():
    heap = Min_Heap()
    heap.insert(4)
    heap.insert(50)
    heap.insert(7)
    heap.insert(55)
    heap.insert(90)
    heap.insert(87)
    heap.insert(2)
    print(heap.data)
    print(heap.extract_min())
    print(heap.data)

test()
