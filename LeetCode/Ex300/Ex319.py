exe_count = 0
class Ex319(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int(math.sqrt(n))
        
    def bulbSwitch4(self, n):
        """
        :type n: int
        :rtype: int
        """
        # O(nlgn)
        import math
        if n <= 1:
            return n
        A = [True] * n
        i = 2
        exe_count = 0
        half = int(math.ceil(n / 2))
        #half = n
        while i <= half:
            count = 0
            t = n / i
            j = i * 1
            while count < t:
                
                A[j-1] = not A[j-1]
                j += i
                count += 1                
                exe_count += 1
            i += 1
            #print 82, exe_count
        
        print 82, exe_count, half
        print 83, A[:half].count(True)
        start = half
        res = n - start - A[start:].count(True)
        
        return A[:start].count(True) + res
        
    def bulbSwitch3(self, n):
        """
        :type n: int
        :rtype: int
        """
        # O(nlgn)
        import math
        if n <= 1:
            return n
        A = [1] * n
        i = 2
        exe_count = 0
        half = int(math.ceil(n / 2))
        half = n
        while i <= half:
            count = 0
            t = n / i
            j = i * 1
            while count < t:
                if A[j-1] == 1:
                    A[j-1] = 0
                else:
                    A[j-1] = 1
                j += i
                count += 1                
                exe_count += 1
            i += 1
            #print 82, exe_count
        
        #print 105, exe_count, half
        start = half
        res = n - start - sum(A[start:])
        
        return sum(A[:start]) + res
        
        
    def count_factor(self, n):
        import math
        count = 0
        root = math.ceil(math.sqrt(n))
        root = int(root)
        global exe_count
        for i in range(1, root):
            exe_count += 1
            if n % i == 0:
                #print 62, n, i, root
                count += 2
        if root ** 2 == n:
            #print 65, math.sqrt(n)
            count += 1
        return count
        
    def bulbSwitch1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # O(n**1.5)
        #global exe_count
        import math
        if n == 0:
            return 0
        A = [0] * n
        root = math.ceil(math.sqrt(n))
        root = int(root)
        for i in range(n):
            count = self.count_factor(i + 1)
            #print 126, i, count, root
            if count % 2 == 1:
                A[i] = 1
            #print 129, A
        
        #print 113, exe_count
        return sum(A)
        
    def bulbSwitch0(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Slow O(n2)
        if n == 0:
            return 0
        A = [1] * n
        i = 2
        while i <= n:
            for j in range(i-1, n):
                if (j+1) % i == 0:
                    if A[j] == 0:
                        A[j] = 1
                    else:
                        A[j] = 0
            i += 1
            
        #return A
        return sum(A)
        
ex319 = Ex319()
#print 319, ex319.count_factor(17)
print 319, ex319.bulbSwitch1(999)

