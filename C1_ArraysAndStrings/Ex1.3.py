def URLify(string, l):
    res = []
    has_add = False
    for a in string:
        if a != ' ':
            has_add = False
            res.append(a)
        elif a == ' ' and not has_add:
            has_add = True
            res.append('%20')
    '''
    if res[-1] == '%20':
        res.pop(-1)
    '''
    res = ''.join(res[:l])
    return res.rstrip()

def URLify2(string, l):
    i = 0
    res = []
    has_add = False
    for a in string:
        if i > l:
            break
        if string[i] != ' ':
            res.append(string[i])
            has_add = False
            i += 1
        else:
            if not has_add:
                res.append('%20')
                has_add = True
                i += 1
    return ''.join(res)

print(URLify('Mr John Smith   ', 13))
