def permu_palin(string):
    dic = {}
    for a in string:
        a = a.lower()
        if a not in dic:
            dic[a] = 1
        else:
            dic[a] += 1
    found_odd = False
    for k, v in dic.items():
        if k == ' ':
            continue
        if v % 2 == 1:
            if not found_odd:
                found_odd = True
            else:
                return False
    return True

print(permu_palin('Tact Coa'))
