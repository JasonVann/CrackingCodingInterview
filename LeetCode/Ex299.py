class Ex299(object):    
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        to_check = []
        s = str(secret)
        g = str(guess)
        cA = 0
        cB = 0
        dic = {}
        for i in range(len(s)):
            if s[i] == g[i]:
                cA += 1
            else:
                if s[i] in dic:
                    dic[s[i]] += [i]
                else:
                    dic[s[i]] = [i]
                to_check.append(i)
        #print 23, dic, to_check
        for j in to_check:
            if g[j] in dic:
                cB += 1
                a = dic[g[j]]
                a.pop(0)
                if a == []:
                    dic.pop(g[j])
        res = str(cA) + 'A' + str(cB) + 'B'
        return res
    '''
    public String getHint(String secret, String guess) {
        int bulls = 0;
        int cows = 0;
        int[] numbers = new int[10];
        for (int i = 0; i<secret.length(); i++) {
            int s = Character.getNumericValue(secret.charAt(i));
            int g = Character.getNumericValue(guess.charAt(i));
            if (s == g) bulls++;
            else {
                if (numbers[s] < 0) cows++;
                if (numbers[g] > 0) cows++;
                numbers[s] ++;
                numbers[g] --;
            }
        }
        return bulls + "A" + cows + "B";
    }
    '''

