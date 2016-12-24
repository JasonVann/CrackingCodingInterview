class Ex204(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # set
        exe_count = 0
        if n <= 1:
            return 0
        prime = set(range(2, n, 1))
        #prime = [True] * (n-1)
        #prime[0] = False
        i = 2
        #exe_count = 0
        
        while i * i < n:
            if i not in prime:
                i += 1
                continue
            j = i * i
            #j += i
            while j < n:
                #print 72, i, j
                if j in prime:
                    prime.remove(j)
                #prime[j-1] = False
                j += i     
                exe_count += 1
            i += 1
            
        #print 82, exe_count
        #print 89, prime, i, j
        return len(prime)
        
    def countPrimes3(self, n):
        """
        :type n: int
        :rtype: int
        """
        exe_count = 0
        if n <= 1:
            return 0
        #prime = set(range(2, n, 1))
        prime = [True] * (n-1)
        prime[0] = False
        i = 2
        #exe_count = 0
        
        while i * i < n:
            if not prime[i-1]:
                i += 1
                continue
            j = i * i
            #j += i
            while j < n:
                #print 72, i, j
                #if j in prime:
                    #prime.remove(j)
                prime[j-1] = False
                j += i     
                exe_count += 1
            i += 1
            
        #print 82, exe_count
        count = 0
        for i in prime:
            if prime[i] == True:
                count += 1
        #print 89, prime, i, j
        return count
        
    def is_prime(self, n):
        if n < 2:
            return False
        i = 2
        while i < n:
            if n % i == 0:
                return False
            i += 1
        return True
        
    def remove_cand(self, not_cand, i, n):
        global exe_count
        j = i * i
        import math
        n0 = math.sqrt(n)
        while j <= n0:
            #if j not in not_cand:
            exe_count += 1
            if j % 2 == 1:
                not_cand.add(j)
            j += i
            
    def countPrimes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        global exe_count
        if n <= 1:
            return 0
        composite = set(range(2, n, 2))
        composite.add(1)
        not_cand = set()
        
        i = 3
        #exe_count = 0
        while i < n:
            if i in not_cand:
                i += 2
                continue
                
            j = i * 2
            #j += i
            while j < n:
                if j not in composite:
                    composite.add(j)
                j += i     
                exe_count += 1
            self.remove_cand(not_cand, i, n)
            i += 2
            
        print 82, exe_count
        
        #print 89, composite
        return n - 1 - len(composite)
        
    def countPrimes0(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        composite = set([1])
        i = 2
        exe_count = 0
        while i < n:
            #t = n / i
            j = i * 2
            '''
            if j not in composite:
                if not self.is_prime(j):
                    composite.add(j)
            '''
            #j += i
            while j < n:
                if j not in composite:
                    composite.add(j)
                j += i     
                exe_count += 1
            i += 1
        print 82, exe_count
        
        #print 89, composite
        return n - 1 - len(composite)
    '''
    class Solution {
    public:
        int countPrimes(int n) {
            vector<bool> prime(n, true);
            prime[0] = false, prime[1] = false;
            for (int i = 0; i < sqrt(n); ++i) {
                if (prime[i]) {
                    for (int j = i*i; j < n; j += i) {
                        prime[j] = false;
                    }    
                }    
            }
            return count(prime.begin(), prime.end(), true);
        }
    };
    '''
    
ex204 = Ex204()
n = 10
n = 499997
#print 204, ex204.is_prime(n)
print 204, ex204.countPrimes(n), time.time() - start_time

