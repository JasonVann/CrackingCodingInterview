class Ex49(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for a in strs:
            temp = list(a)
            temp.sort()
            temp = ''.join(temp)
            if temp in dic:
                dic[temp].append(a)
            else:
                dic[temp] = [a]
        return dic.values()
    '''
    ???
    def groupAnagrams(self, strs):
        groups = itertools.groupby(sorted(strs, key=sorted), sorted)
        return [sorted(members) for _, members in groups]
    '''
    '''
    # Counting Sort
    string strSort(string& s) {
        int count[26] = {0}, n = s.length();
        for (int i = 0; i < n; i++)
            count[s[i] - 'a']++;
        int p = 0;
        string t(n, 'a');
        for (int j = 0; j < 26; j++)
            for (int i = 0; i < count[j]; i++)
                t[p++] += j;
        return t;
    } 
    '''

