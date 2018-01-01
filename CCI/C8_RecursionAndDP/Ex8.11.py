def count_coin(n):
    # Represent n cents with 25c, 10c, 5c, 1c
    A = [{}] * (n+1)
    A[0][(1, )] = 1
    coins = (1, 5, 10, 25)
    res = count(n, A, coins)
    print(A)
    return res

def count(n, cache, coins):
    if n < 0:
        return 0
    if n == 0:
        return 1
    '''
    if coins in cache[n]:
        return cache[n][coins]
    '''
    temp = 0
    if 25 in coins:
        c25 = count(n-25, cache, coins)
        temp += c25
    if 10 in coins:
        #c10 = count(n-10, cache, [c for c in coins if c != 25])
        c10 = count(n-10, cache, (1, 5, 10))
        temp += c10
    if 5 in coins:
        #c5 = count(n-5, cache, [c for c in coins if c not in [10, 25]])
        c5 = count(n-5, cache, (1, 5))
        temp += c5
    c1 = count(n-1, cache, (1, ))
    temp += c1
    cache[n][coins] = temp
    return temp

# 10, 5*2, 1*10, 5+1*5
print(count_coin(16))
#print(count_coin(35))
#print(count_coin(5))
