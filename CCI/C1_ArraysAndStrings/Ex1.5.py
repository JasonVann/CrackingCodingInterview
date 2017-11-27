def one_away(a, b):
    if abs(len(a) - len(b)) > 1:
        return False

    i = 0
    j = 0
    while i < len(a):
        if j == len(b) and i == len(a) - 1:
            return True
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            #print 14, a[i:], b[j:], i, j
            if a[i+1:] == b[j:]:
                # i is an addition
                return True
            elif a[i+1:] == b[j+1:]:
                # i is an edit
                return True
            else:
                return False
    return True

print one_away('pale', 'ple')
print one_away('pales', 'pale')
print one_away('pale', 'bale')
print one_away('pale', 'bake')
print one_away('pale', 'pales')
print one_away('pale', 'palts')
