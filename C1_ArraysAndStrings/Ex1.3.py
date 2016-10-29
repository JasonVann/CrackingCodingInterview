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

print URLify('Mr John Smith   ', 13)
            
            
