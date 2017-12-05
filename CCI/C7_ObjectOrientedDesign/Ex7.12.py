class HashTable():
    def __init__(self, N):
        self.data = [None] * N

    def hash(self, i):
        return (i+19423) % N

    def insert(self, k, v):
        index = self.hash(k)
        if self.data[index] is None:
            self.data[index] = [(k, v)]
        else:
            self.data[index] += [(k, v)]
