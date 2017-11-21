class Ex454(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """    
        # Optimized hashmap
        count = 0
        n = len(A)
        if n == 0:
            return 0
        count = 0
        n = len(A)
        if n == 0:
            return 0
        sum1 = {}
        sum2 = {}
        for i in A:
            for j in B:
                temp = i + j
                if temp in sum1:
                    sum1[temp] += 1
                else:
                    sum1[temp] = 1
        for i in C:
            for j in D:
                temp = i + j
                if -temp in sum1:
                    count += sum1[-temp]
                    
        return count
        
    def fourSumCount0(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """     
        # O(n2)
        count = 0
        n = len(A)
        if n == 0:
            return 0
        sum1 = {}
        sum2 = {}
        for i in A:
            for j in B:
                temp = i + j
                if temp in sum1:
                    sum1[temp] += 1
                else:
                    sum1[temp] = 1
        for i in C:
            for j in D:
                temp = i + j
                if temp in sum2:
                    sum2[temp] += 1
                else:
                    sum2[temp] = 1
        for k, v in sum1.items():
            if -k in sum2:
                temp = v * sum2[-k]
                count += temp
        return count
    '''    
    def fourSumCount(self, A, B, C, D):
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)
    '''

