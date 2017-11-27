class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def sum_list(a, b):
    # assume num in reversed order
    # 1234 + 567: 4->3->2->1 + 7->6->5
    if a == None:
        return b
    if b == None:
        return a
    res = Node(0)
    next = Node(0)
    carry = 0
    head = res
    res2= res

    while True:
        if a == None and b == None:
            break
        if a == None:
            temp = b.val + carry
        elif b == None:
            temp = a.val + carry
        else:
            temp = a.val + b.val + carry
        carry = 0
        if temp > 9:
            (carry, temp) = (temp//10, temp%10)

        res2 = Node(temp)
        res.next = res2
        res = res.next
        if a != None:
            a = a.next
        if b != None:
            b = b.next
    if carry:
        res.next = Node(carry)
    return head.next
    '''
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
    '''

def sum_recur_rev(a, b):
    # Reverse: 1234 + 567: 4->3->2->1 + 7->6->5
    def recur(a, b, carry):
        if a == None:
            return b
        if b == None:
            return a

        a.val = a.val + b.val + carry
        carry = 0
        if a.val > 9:
            a.val -= 10
            carry = 1
        node = recur(a.next, b.next, carry)
        if node == None and carry:
            a.next = Node(1)
        else:
            a.next = node
        return a
    return recur(a, b, 0)

def sum_recur(a, b):
    # 4321 + 7659: 4->3->2->1 + 0->7->6->5
    def recur(a, b):
        if a == None:
            return 0, None
        carry, temp = recur(a.next, b.next)
        a.next = temp
        a.val = a.val + b.val + carry
        carry = 0
        if a.val > 9:
            a.val -= 10
            carry = 1
        return carry, a

    la = get_len(a)
    lb = get_len(b)
    if la < lb:
        la, lb = lb, la
        a, b = b, a
    if la > lb:
        temp = Node(0)
        b_head = temp
        for i in range(la-lb-1):
            temp.next = Node(0)
            temp = temp.next
        temp.next = b
        b = b_head
    # Now a, b have the same length
    carry, temp = recur(a, b)
    if carry:
        res = Node(1)
        res.next = temp
    return res

def get_len(a):
    l = 0
    while a:
        l += 1
        a = a.next
    return l

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
#b2.next = b3
print(get_len(b0))
#res = sum_list(b0, a0)
#res = sum_recur_rev(a0, b0)
res = sum_recur(b0, a0)
print(res)
