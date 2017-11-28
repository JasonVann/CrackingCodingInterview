import queue
from queue import Queue

class Animal_Shelter():
    def __init__(self):
        self.dog = Queue()
        self.cat = Queue()

    def enqueue(self, t, animal):
        if t == 'dog':
            self.dog.push(animal)
        elif t == 'cat':
            self.cat.push(animal)
        else:
            raise Exception('Unknown Animal')

    def dequeue_cat(self):
        if self.cat.is_empty():
            return None
        return self.cat.pop()

    def dequeue_dog(self):
        if self.dog.is_empty():
            return None
        return self.dog.pop()

    def peek_dog(self):
        if self.dog.is_empty():
            return None
        return self.dog.peek()

    def peek_cat(self):
        if self.cat.is_empty():
            return None
        return self.cat.peek()

    def dequeue_any(self):
        dog = self.peek_dog()
        cat = self.peek_cat()
        if not cat:
            return self.dequeue_dog()
        if not dog:
            return self.dequeue_cat()
        if dog < cat:
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

def test():
    shelter = Animal_Shelter()
    print(shelter.dequeue_any())
    shelter.enqueue('dog', 1)
    print(shelter.dequeue_cat())
    shelter.enqueue('dog', 4)
    shelter.enqueue('cat', 2)
    shelter.enqueue('cat', 3)
    print(shelter.dequeue_any())
    print(shelter.dequeue_any())

test()
