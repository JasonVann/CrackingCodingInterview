class Ex290(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {}
        words = str.split(' ')
        print str, words
        for i in range(len(pattern)):
            if i >= len(words):
                return False
            if pattern[i] not in dic:
                dic[pattern[i]] = words[i]
            else:
                if dic[pattern[i]] != words[i]:
                    return False
        dic2 = {}
        for i in range(len(words)):
            if i >= len(pattern):
                return False
            if words[i] not in dic2:
                dic2[words[i]] = pattern[i]
            else:
                if dic2[words[i]] != pattern[i]:
                    return False
        return True
        
ex290 = Ex290()
p = "abba"
str2= "dog dog dog dog"
print 290, ex290.wordPattern(p, str2)

'''
def wordPattern(self, pattern, str):
    s = pattern
    t = str.split()
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
    
public boolean wordPattern(String pattern, String str) {
    String[] words = str.split(" ");
    if (words.length != pattern.length())
        return false;
    Map index = new HashMap();
    for (Integer i=0; i<words.length; ++i)
        if (index.put(pattern.charAt(i), i) != index.put(words[i], i))
            return false;
    return true;
}
'''
