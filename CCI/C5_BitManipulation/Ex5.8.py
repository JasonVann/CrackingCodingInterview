def draw_line(A, w, x1, x2, y):
    # Draw a line from (x1, y) to (x2, y)
    # A is a list of byte
    row = w/8
    y_start = row*y
    x_start = y_start + x1//8 # first full byte
    if x1 % 8 != 0:
        x_start += 1
    #k1 = 1 << (x1%8) - 1
    all_ones = 2**8-1
    last_full_byte = x2 / 8
    if x2 % 8 != 7:
        last_full_byte -= 1
    k1 = all_ones >> (x1 % 8)
    i = 0
    #for i in range((x2-x1+1)//8):
    while x_start + i < = last_full_byte:
        A[x_start + i] = all_ones
        i += 1
    k2 = all_ones - (all_ones >> (x2%8+1)
    if x1 / 8 == x2 / 8:
        # same byte
        A[x_start] |= k1 | k2
    else:
        if x1 % 8:
            A[x_start] |= k1
        if x2 % 8 != 7:
            A[y_start + x2//8] |= k2
    return A
