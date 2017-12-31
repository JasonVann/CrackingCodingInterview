def group_anagrams(A):
    lookup = {}
    for a in A:
        temp = ''.join(sorted(a))
        if temp not in lookup:
            lookup[temp] = [a]
        else:
            lookup[temp] += [a]
    i = 0
    for k, v in lookup.items():
        for temp in v:
            A[i] = temp
            i += 1
    return A

def test():
    A = ['dog', 'bca', 'cba', 'god', 'efs']
    print(group_anagrams(A))

test()
