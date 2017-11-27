def toggle(bit_vector: int, index):
    # Toggle bit_vector[index] on/off
    print(bit_vector, bin(bit_vector), index)
    mask = 1 << index
    if bit_vector & mask == 0:
        bit_vector |= mask
    else:
        bit_vector &= ~mask
    print(bin(bit_vector))
    return bit_vector

def check_exactly_one_bit_set(bit_vector: int):
    return bit_vector & (bit_vector-1) == 0

print(toggle(1234, 2))
print(toggle(1234, 1))
print(check_exactly_one_bit_set(15))
