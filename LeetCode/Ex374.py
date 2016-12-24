# Ex374
target = 10
def guess(n, target):
    if n > target:
        return -1
    elif n < target:
        return 1
    else:
        return 0
