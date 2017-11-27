class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def sum_list(a, b):
    # assume num in reversed order
    if a == None:
        return b
    if b == None:
        return a
    res = Node(None)
    next = Node(None)
    carry = 0
    head = res
    res2= res
    
    while a != None and b != None:
        res = res2
        temp = a.val + b.val + carry
        if temp > 10:
            (carry, temp) = (temp/10, temp%10)

        res.val = temp
        res2 = Node(None)
        res.next = res2
       
        a.next = a
        b.next = b
    has_add = False
    if a != None:
        has_add = True
        res.next = a
    if b != None:
        res.next = b
        has_add = True
    if has_add:
        res.val = res.val + carry
        if res.val > 10:
            res2 = None(None)
            (carry, temp) = (temp/10, temp%10)
            res.val = temp
            res2.val = carry
            res.next = res2
            res2.next = None
    return head

