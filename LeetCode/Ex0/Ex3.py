class Ex3(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return n
            
        res = 0
        i = 0
        j = i + 1
        temp = set([s[i]])
        #for i in range(n):
        while i < n:            
            
            while j < n:
                if s[j] not in temp:
                    temp.add(s[j])
                    j += 1
                else:
                    break
                
            count = j - i
            if count > res:
                res = count 
            print 75, count, j, i, temp, res
            
            if s[i] not in s[i+1:j]:
                temp.remove(s[i])
            
            print 80, temp, i, s[i], s[i+1:j]
            i = i + 1
            #j = j + 1
        return res
        
    def lengthOfLongestSubstring0(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Slow
        dic = {}
        for i in range(len(s)):
            e = s[i]
            if e in dic:
                dic[e] += [i]
            else:
                dic[e] = [i]
        res = 0
        temp = 0
        n = len(s)
        A = [1] * len(s)
        start = None
        for i in range(len(s)):
            e = s[i]
            j = dic[e].index(i)
            if j < len(dic[e]) - 1:
                #print 76, e, j, dic[e], len(dic[e])
                j = dic[e][j + 1] - i
            else:
                j = n - i
            if start == None:
                start = i
            A[i] = j
        for i in range(n):
            j = A[i]
            temp = j
            for k in range(i+1, i+j):
                #print 87, j, A[i], k, A[k], temp, res
                if A[k] + k - i < temp:
                    temp = A[k] + k - i
            if temp > res:
                res = temp
                
        print 82, dic, A, res
        return res
    '''
    public int lengthOfLongestSubstring(String s) {
        if (s.length()==0) return 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max=0;
        for (int i=0, j=0; i<s.length(); ++i){
            if (map.containsKey(s.charAt(i))){
                j = Math.max(j,map.get(s.charAt(i))+1);
            }
            map.put(s.charAt(i),i);
            max = Math.max(max,i-j+1);
        }
        return max;
    }
    '''
        
ex3 = Ex3()

#s = "c"
s = "pwwkew"
s = "abcabcbb"
s = ""
print 3, ex3.lengthOfLongestSubstring(s)

