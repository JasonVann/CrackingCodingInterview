from stack import Stack

def sort_stack(stack):
    bak = Stack()
    size = stack.size
    i = 0
    if size == 0:
        return stack
    temp = stack.pop()
    for i in range(size-1):
        data = stack.pop()
        if data > temp:
            bak.push(temp)
            temp = data
        else:
            j = 0
            if bak.is_empty():
                bak.push(data)
            else:
                while True:
                    data2 = bak.pop()
                    if data2 > data:
                        stack.push(data2)
                        j += 1
                    else:
                        bak.push(data2)
                        bak.push(data)
                        for k in range(j):
                            bak.push(stack.pop())
                        break
    stack.push(temp)
    while not bak.is_empty():
        stack.push(bak.pop())
    return stack

def test():
    s = Stack()
    s.push(4)
    s.push(5)
    s.push(1)
    s.push(2)
    s.push(21)
    s.push(-2)
    s = sort_stack(s)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

test()
