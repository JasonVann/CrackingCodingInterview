def magic_index(A):
    # A[i] = i
    l = 0
    r = len(A)
    while l < r:
        mid = int((l+r)/2)
        if A[mid] > mid:
            r = mid - 1
        elif A[mid] < mid:
            l = mid + 1
        else:
            return mid
    return -1
