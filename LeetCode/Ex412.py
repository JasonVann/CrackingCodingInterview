class Ex412(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                cur = 'FizzBuzz'
            elif i % 3 == 0:
                cur = 'Fizz'
            elif i % 5 == 0:
                cur = 'Buzz'
            else:
                cur = str(i)
            res.append(cur)
        return res
    '''
    return [str(i) if (i%3!=0 and i%5!=0) else (('Fizz'*(i%3==0)) + ('Buzz'*(i%5==0))) for i in range(1,n+1)]
    '''

