def insert_bits2(N, M, i, j):
    # N, M: int
    # Replace N[j, i] with M
    count = j - i
    for k in range(count, -1, -1):
        shift = j - (count-k)
        m = M >> k
        mask = ~(1<<shift)
        N = N & mask
        a = bin(N)
        N = N | (m<<shift)
        b = bin(N)
    return N

def insert_bits_sol(N, M, i, j):
    left = (~0) << (j+1)
    right = ((1<<i)-1)
    mask = left | right
    N = N & mask
    N = N | (M << i)
    return N

def test():
    N=int('10001010100', 2)
    M=int('10011', 2)
    print(N, M)
    #res = insert_bits2(N, M, 2, 6)
    res = insert_bits_sol(N, M, 2, 6)
    print(res, N, bin(res))

test()
