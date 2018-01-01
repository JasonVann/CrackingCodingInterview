def triple_step(n):
    # n steps to climb, with a step size of 1,2,3
    if n < 1:
        return 0
    A = [0] * (n+1)
    A[0] = 1
    for i in range(1, n+1):
        temp = A[i-1]
        if i-2 >= 0:
            temp += A[i-2]
        if i - 3 >= 0:
            temp += A[i-3]
        A[i] = temp
    #print(A)
    return A[-1]

#print(triple_step(0))
#print(triple_step(1))
#print(triple_step(2))
print(triple_step(37))
