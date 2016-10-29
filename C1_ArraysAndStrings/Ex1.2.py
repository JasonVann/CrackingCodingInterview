def check_permu(a, b):
    if len(a) != len(b):
        return False
    dic = {}
    for i in b:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for j in a:
        if j not in dic:
            return False
        else:
            dic[j] -= 1
            if dic[j] == 0:
                dic.pop(j)
    return True

a = 'abcdef'
b = 'bcfeda'
a = 'abaa'
b = 'abac'
print check_permu(a, b)
