class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = bin(n)[2:]
        count = 0
        for c in res:
            if c == '1':
                count += 1
        return count
        
'''
int hammingWeight(uint32_t n)
{
    int res = 0;
    while(n)
    {
        n &= n - 1;
        ++ res;
    }
    return res;
}
Each time of "n &= n - 1", we delete one '1' from n.
'''
