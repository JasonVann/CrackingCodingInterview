class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def get_len(a):
    l = 0
    while a:
        l += 1
        a = a.next
    return l

def intersect(a, b):
    la = get_len(a)
    lb = get_len(b)
    if la < lb:
        la, lb = lb, la
        a, b = b, a
    if la > lb:
        for i in range(la-lb):
            a = a.next
    while a:
        if a == b:
            return a
        a = a.next
        b = b.next
    return False

def recur(a, b, k):
    # ??
    if a.next == None and b.next == None:
        if a == b:
            return True, 0
        else:
            return False, None

a0 = Node(4)
a1 = Node(3)
a2 = Node(2)
a3 = Node(1)
a0.next = a1
a1.next = a2
a2.next = a3
b0 = Node(8)
b1 = Node(6)
b2 = Node(5)
b3 = Node(9)
b0.next = b1
b1.next = b2
b2.next = b3
b3.next = a2
print(intersect(b0, a0))
