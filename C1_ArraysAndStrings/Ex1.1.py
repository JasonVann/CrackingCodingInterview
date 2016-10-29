def is_unique(string):
    # This doesn't quit work
    res = 0
    for a in string:
        res = res^ord(a)
    print res
    return res != 0

print is_unique('abcdefg')
print is_unique('abcadefg')
