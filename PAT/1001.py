def count(n, c):
    if n == 1:
        return c
    if n % 2 == 0:
        return count(n/2, c+1)
    else:
        return count((3*n+1)/2, c+1)
import sys
def main(n):
    return count(n, 0)
n = sys.argv

print main(n)
