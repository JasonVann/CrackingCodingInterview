def count_bits(a, b):
    res = a ^ b
    # then count 1s in res
    i = 0
    while res > 0:
        if res & 1:
            i += 1
        res >>= 1
    return i

def count_bits_sol(a, b):
    res = a ^ b
    # then count 1s in res
    i = 0
    while res > 0:
        i += 1
        res = res & (res-1)
    return i

def test():
    print(count_bits(29, 15))
    print(count_bits_sol(29, 15))

test()
