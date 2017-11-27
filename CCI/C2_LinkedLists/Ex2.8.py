class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def loop(a):
    fast = a
    slow = a
    if fast is None:
        return False

    while True:
        if fast.next is None:
            return False
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    # Now fast the i nodes away from the intersection
    slow2 = a
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow

a0 = Node(1)
a1 = Node(2)
a2 = Node(3)
a3 = Node(4)
a0.next = a1
a1.next = a2
a2.next = a3
b0 = Node(5)
b1 = Node(6)
b2 = Node(7)
b3 = Node(8)
a3.next = b0
b0.next = b1
b1.next = b2
b2.next = b3
b3.next = a3
print(loop(a0))
