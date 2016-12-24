def list_permute2(lst, res):
    if res == nil:
        pass
    if len(lst) == 2:
        res.append([lst[0], lst[1]])
        res.append([lst[1], lst[0]])
    elif len(lst) == 1:
        res.append([lst[0]])
    elif len(lst) == 0:
        print 'No data'
    else:
        pass
    #print res
    
def permutations(head, tail=''):
    if len(head) == 0: print tail
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i+1:], tail+head[i])
            
permutations('123')
#list_permute([1,2],[])
