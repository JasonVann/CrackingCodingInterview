class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def delete(node):
    next_node = node.next
    while next_node != None:
        node.val = next_node.val
        prev = node
        node = node.next
        next_node = next_node.next
    prev.next = None

def delete_sol(node):
    if node == None or node.next == None:
        return
    next_node = node.next
    node.val = next_node.val
    node.next = next_node.next
    return
