class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_K_last(head, k):
    node = head
    l = 1
    while node.next:
        l += 1
        node = node.next
    node = head
    for i in range(l-k):
        node = node.next
    return node

def remove_K_last2(head, k):
    fast = head
    slow = head
    for i in range(k):
        if fast.next is None:
            # k > length
            return None
        fast = fast.next
    while fast.next != None:
        fast = fast.next
        slow = slow.next
    return slow

def remove_K_last_recur(head, k):
    if head.next is None:
        return 0, None
    num, node = remove_K_last_recur(head.next, k)
    num += 1
    if num == k:
        print(head.val)
        return num, head
    return num, head
