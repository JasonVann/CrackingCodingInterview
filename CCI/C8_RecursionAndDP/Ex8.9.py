def parens(n):
    # Generate all valid n pairs of parentheses
    cache = {}
    if n == 0:
        return ''
    cache[1] = set(['()'])
    for i in range(2, n+1):
        v1 = ['()' + c for c in cache[i-1]]
        v2 = ['('+ c + ')' for c in cache[i-1]]
        v3 = [c + '()' for c in cache[i-1]]
        temp = v1 + v2 + v3
        cache[i] = set(temp)
    return cache[n]

print(parens(3))
print(parens(6))
