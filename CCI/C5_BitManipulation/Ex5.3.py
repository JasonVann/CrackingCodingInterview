def flip_bit(num):
    num = bin(num)[2:]
    lookup = [0]
    if '0' not in num:
        return len(num)
    for index, i in enumerate(num):
        if i == '0':
            lookup.append(index+1)
    # Add the index for final hidden '0'
    lookup.append(index+1)
    max = 0
    print(lookup)

    for i in range(1, len(lookup)-1):
        temp = lookup[i+1] - lookup[i-1]
        if temp > max:
            max = temp
    return max

def test():
    print(flip_bit(1775))
    print(flip_bit(7))
    print(flip_bit(157))

test()
