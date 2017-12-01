def print_bin(num):
    # print 0.72 in binary
    i = 0
    res = ['.']
    while i < 32:
        num = num * 2
        c,  num = str(int(num // 1)), num%1
        res.append(c)
        if num == 0:
            break
        i += 1
    res = ''.join(res)
    print(res)
    if num == 0:
        return res
    return 'ERROR'

def test():
    print(print_bin(0.72))
    print(print_bin(0.75))

test()
