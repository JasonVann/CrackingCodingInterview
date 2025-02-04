class Ex242(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        s1 = list(s)
        s1.sort()
        t1 = list(t)
        t1.sort()
        return s1 == t1
        
    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        dic = {}
        for a in s:
            if a in dic:
                dic[a] += 1
            else:
                dic[a] = 1
        for b in t:
            if b not in dic:
                return False
            dic[b] -= 1
            if dic[b] < 0:
                return False
        return True
        
        s1 = list(s)
        s1.sort()
        t1 = list(t)
        t1.sort()
        return s1 == t1
    '''
    public class Solution {
        public List<Integer> findAnagrams(String s, String p) {
            List<Integer> list = new ArrayList<>();
        if (s == null || s.length() == 0 || p == null || p.length() == 0) return list;
        
        int[] hash = new int[256]; //character hash
        
        //record each character in p to hash
        for (char c : p.toCharArray()) {
            hash[c]++;
        }
        //two points, initialize count to p's length
        int left = 0, right = 0, count = p.length();
        
        while (right < s.length()) {
            //move right everytime, if the character exists in p's hash, decrease the count
            //current hash value >= 1 means the character is existing in p
            if (hash[s.charAt(right)] >= 1) {
                count--;
            }
            hash[s.charAt(right)]--;
            right++;
            
            //when the count is down to 0, means we found the right anagram
            //then add window's left to result list
            if (count == 0) {
                list.add(left);
            }
            //if we find the window's size equals to p, then we have to move left (narrow the window) to find the new match window
            //++ to reset the hash because we kicked out the left
            //only increase the count if the character is in p
            //the count >= 0 indicate it was original in the hash, cuz it won't go below 0
            if (right - left == p.length() ) {
               
                if (hash[s.charAt(left)] >= 0) {
                    count++;
                }
                hash[s.charAt(left)]++;
                left++;
            
            }

            
        }
            return list;
        }
    }
    '''

