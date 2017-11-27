class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def partition(head, k):
    # all nodes smaller than k, k, larger than k
    small = None
    large = None
    node = head
    while node:
        if node.val < k:
            if small:
                small.next = node
            else:
                small = node
            small = small.next
        else:
            if large:
                large.next = node
            else:
                large = node
                partition = node
            large = large.next
        node = node.next
    if not small:
        return partition
    small.next = partition
    if large:
        large.next = None
    return head
