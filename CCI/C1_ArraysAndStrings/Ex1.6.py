def str_compress(string):
    res = []
    i = 0
    j = 1
    while i < len(string):
        #print j, i
        if j < len(string) and string[i] == string[j]:
            j+=1
        else:
            temp = str(string[i]) + str(j-i)
            res.append(temp)
            i = j
            j += 1
    res = ''.join(res)
    #print res
    if len(res) >= len(string):
        return string
    return res

print str_compress('abc')
print str_compress('aabcccccaaa')
