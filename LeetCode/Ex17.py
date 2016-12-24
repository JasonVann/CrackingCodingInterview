class Ex17(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {}
        dic['2'] = ['a', 'b', 'c']
        dic['3'] = ['d', 'e', 'f']
        dic['4'] = ['g', 'h', 'i']
        dic['5'] = ['j', 'k', 'l']
        dic['6'] = ['m', 'n', 'o']
        dic['7'] = ['p', 'q', 'r', 's']
        dic['8'] = ['t', 'u', 'v']
        dic['9'] = ['w', 'x', 'y', 'z']
        res = []
        while len(digits) > 0:
            cur = digits[0]
            digits = digits[1:]
            if res == []:
                res += dic[cur]
            else:
                next = dic[cur]
                #print 74, cur, next, res
                res = [a + b for a in res for b in next]
                '''
                if isinstance(res[0], str):
                    res = [[a] + [b] for a in res for b in next]
                else:
                    res = [a + [b] for a in res for b in next]
                '''
        '''     
        res2 = []
        #print 79, res
        for a in res:
            a = a[::-1]
            temp = reduce(lambda x, y: x + y, a)
            res2.append(temp)
        '''
        return res
    '''
    public List<String> letterCombinations(String digits) {
        LinkedList<String> ans = new LinkedList<String>();
        String[] mapping = new String[] {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        ans.add("");
        for(int i =0; i<digits.length();i++){
            int x = Character.getNumericValue(digits.charAt(i));
            while(ans.peek().length()==i){
                String t = ans.remove();
                for(char s : mapping[x].toCharArray())
                    ans.add(t+s);
            }
        }
        return ans;
    }
    '''
        
ex17 = Ex17()
print 17, ex17.letterCombinations('23')
