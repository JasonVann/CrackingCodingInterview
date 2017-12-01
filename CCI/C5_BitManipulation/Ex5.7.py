def swap(n):
    # Swap adjacent odd bits with even bits
    # 011010->100101
    mask1 = int('aaaaaaaa', 16)
    mask2 = int('55555555', 16)
    return ((n & mask1) >> 1) | ((n & mask2) << 1)

def test():
    print(swap(26))

test()
