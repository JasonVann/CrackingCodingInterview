def is_substring(a, b):
    return a in b

def string_rotate(a, b):
    # Bug:
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if a[i:] in b:
            if a[:i] in b:
                return True
    return False

def string_rotate2(a, b):
    if len(a) != len(b):
        return False
    if a in b + b:
        return True
    return False

print string_rotate('eottle', 'bottle') # Bug
print string_rotate2('waterbottle', 'erbottlewat')
print string_rotate2('waterbottle', 'erbottlewae')
