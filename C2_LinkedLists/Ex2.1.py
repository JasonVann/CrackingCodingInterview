class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
def remove_dup(head):
    first = head
    while first.next != None:
        second = first
        while second.next != None:
            if first.val != second.next.val:
                second = second.next
            else:
                second.next = second.next.next
        first = fist.next
        
    return head
