class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def is_palindrome(a):
    def recur(node, middle1, middle2):
        if node.next != middle1 and node.next != middle2:
            res, next_node = recur(node.next, middle1, middle2)
        else:
            return node.val == middle2.next.val, middle2.next
        if not res:
            return False, None
        if res:
            if node.val == next_node.next.val:
                return True, next_node.next
            else:
                return False, None

    fast = a
    slow = a
    prev = a
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    if fast:
        # Odd # of node
        left = slow
        right = slow
    else:
        left = prev
        right = slow
    res, node = recur(a, left, right)
    return res

def test_even_node():
    a0 = Node('A')
    a1 = Node('B')
    a11 = Node('E')
    a2 = Node('C')
    a20 = Node('C')
    a21 = Node('E')
    a3 = Node('B')
    a4 = Node('A')
    a0.next = a1
    a1.next = a11
    a11.next = a2
    a2.next = a20
    a20.next = a21
    a21.next = a3
    a3.next = a4
    print(is_palindrome(a0))

def test_odd_node():
    a0 = Node('A')
    a1 = Node('B')
    a11 = Node('E')
    a2 = Node('C')
    a21 = Node('E')
    a3 = Node('B')
    a4 = Node('A')
    a0.next = a1
    a1.next = a11
    a11.next = a2
    a2.next = a21
    a21.next = a3
    a3.next = a4
    print(is_palindrome(a0))

test_even_node()
test_odd_node()
