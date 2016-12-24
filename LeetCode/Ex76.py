class Ex76(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 1s
        from collections import deque
        dic = {}
        dic2 = {}
        dic3 = {}
        for a in t:
            dic[a] = deque()
            dic3[a] = 0
            #dic[a] = []
            if a not in dic2:
                dic2[a] = 1
            else:
                dic2[a] += 1
        i = 0
        res = []
        lt = len(t)
        count = 0
        v2 = None
        #found = False
        drop = True
        l = None
        idx_l = None
        while i < len(s):
            cur = s[i]
            if cur in t:
                #if dic[cur] == 0:                
                #if dic2[cur] == len(dic[cur]):
                if dic2[cur] == dic3[cur]:
                    idx_old=dic[cur].popleft()
                    #idx_old = dic[cur].pop(0)
                    if count == lt:
                        drop = True
                else:
                    count += 1
                    dic3[cur] += 1
                dic[cur] += [i]
                if drop and count == lt:
                    #found = True
                    if v2 == None:
                        val = dic.values()
                        v2 = []
                        #v2 = dic.values()
                        
                        for v in val:
                            v2 += v
                        
                        v2.sort()
                        #print 106, v2
                    else:
                        v2.remove(idx_old)
                        v2.append(i)
                        #print 109, v2, s[idx_old], s[i], idx_old, i
                    m = v2[0]
                    n = v2[-1]
                    if res == [] or n - m + 1 < len(res):
                        res = s[m:n+1]
                    #print 88, res, dic, i, len(s)
                    drop = False
                    idx_l = m
                    l = s[m]
                    '''
                    count = 0
                    for k, v in dic.items():
                        dic[k] = []
                    '''
            i += 1
            
        res2 = ''.join(res)
        return len(res2)
     
     
    def minWindow0(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for a in t:
            dic[a] = []
        t1 = len(dic)
        i = 0
        res = []
        count = 0
        while i < len(s):
            cur = s[i]
            if cur in t:
                #if dic[cur] == 0:
                
                if len(dic[cur]) > 0 and t.count(cur) <= len(dic[cur]):
                    dic[cur].pop(0)
                else:
                    count += 1
                dic[cur] += [i]
                if count == len(t):
                    val = dic.values()
                    v2 = []
                    for v in val:
                        v2 += v
                    m = min(v2)
                    n = max(v2)
                    if res == [] or n - m + 1 < len(res):
                        res = s[m:n+1]
                    #print 88, res, dic, i, len(s)
                    '''
                    count = 0
                    for k, v in dic.items():
                        dic[k] = []
                    '''
            i += 1
            
        res2 = ''.join(res)
        return res2
    def minWindow1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        '''
        if len(s) < len(t):
            return ''
        '''
        from collections import deque
        dic = {}
        dic2 = {}
        for a in t:
            #dic[a] = deque()
            dic[a] = []
            if a not in dic2:
                dic2[a] = 1
            else:
                dic2[a] += 1
        i = 0
        res = []
        lt = len(t)
        count = 0
        #found = False
        drop = True
        l = None
        idx_l = None
        while i < len(s):
            cur = s[i]
            if cur in t:
                #if dic[cur] == 0:
                
                if dic2[cur] == len(dic[cur]):
                    #dic[cur].popleft()
                    dic[cur].pop(0)
                    if count == lt and cur == l:
                        drop = True
                else:
                    count += 1
                dic[cur] += [i]
                if drop and count == lt:
                    #found = True
                    val = dic.values()
                    v2 = []
                    for v in val:
                        v2 += v
                    m = min(v2)
                    n = max(v2)
                    if res == [] or n - m + 1 < len(res):
                        res = s[m:n+1]
                    #print 88, res, dic, i, len(s)
                    drop = False
                    idx_l = m
                    l = s[m]
                    '''
                    count = 0
                    for k, v in dic.items():
                        dic[k] = []
                    '''
            i += 1
            
        res2 = ''.join(res)
        return len(res2)
    '''
    string minWindow(string s, string t) {
        vector<int> map(128,0);
        for(auto c: t) map[c]++;
        int counter=t.size(), begin=0, end=0, d=INT_MAX, head=0;
        while(end<s.size()){
            if(map[s[end++]]-->0) counter--; //in t
            while(counter==0){ //valid
                if(end-begin<d)  d=end-(head=begin);
                if(map[s[begin++]]++==0) counter++;  //make it invalid
            }  
        }
        return d==INT_MAX? "":s.substr(head, d);
    }
    '''
    '''
    string minWindow(string S, string T) {
        string result;
        if(S.empty() || T.empty()){
            return result;
        }
        unordered_map<char, int> map;
        unordered_map<char, int> window;
        for(int i = 0; i < T.length(); i++){
            map[T[i]]++;
        }
        int minLength = INT_MAX;
        int letterCounter = 0;
        for(int slow = 0, fast = 0; fast < S.length(); fast++){
            char c = S[fast];
            if(map.find(c) != map.end()){
                window[c]++;
                if(window[c] <= map[c]){
                    letterCounter++;
                }
            }
            if(letterCounter >= T.length()){
                while(map.find(S[slow]) == map.end() || window[S[slow]] > map[S[slow]]){
                    window[S[slow]]--;
                    slow++;
                }
                if(fast - slow + 1 < minLength){
                    minLength = fast - slow + 1;
                    result = S.substr(slow, minLength);
                }
                // shrink the window here
                window[S[slow]]--;
                slow++;
                letterCounter--;
            }
        }
        return result;
    }
    '''
    
ex76 = Ex76()
s = "bdab"
t = "ab"
s = "ADOBECODEBANC"
t = "ABC"
print 76, ex76.minWindow(s, t)

