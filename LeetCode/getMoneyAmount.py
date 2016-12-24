def getMoneyAmount(n):
    """
    :type n: int
    :rtype: int
    """ 
    lo = 1
    high = n
    amount = 0
    while(lo <= high):
        new = (lo + high)/2
        if n-1>1:
            res = guess(new, n-1)
        else:
            res = guess(new, n)
        print new, res
        if(res == 1):
            lo = new + 1
        elif res == -1:
            high = new -1
        else:
            break
        amount += new   
    amount1 = amount
    lo = 1
    high = n
    amount = 0
    #print 'b'
    while(lo <= high):
        new = (lo + high)/2     
        res = guess(new, 1)
        #print new, res
        if(res == 1):
            lo = new + 1
        elif res == -1:
            high = new -1
        else:
            break
        amount += new   
    #print 'c', amount1, amount
    if amount1 > amount:
        print amount1
    else:
        print amount
        
#print getMoneyAmount(4)

