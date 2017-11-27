def is_unique2(string):
    # This doesn't quite work
    res = 0
    for a in string:
        res = res^ord(a)
    print(res)
    return res != 0

def is_unique(string):
    res = set()
    for a in string:
        if a not in res:
            res.add(a)
        else:
            return False
    return True

print(is_unique('abcdefg'))
print(is_unique('abcadefg'))
