class Ex122(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        a = None
        total = 0
        for i in range(1, len(prices)):
            if a == None and prices[i-1] < prices[i]:
                a = prices[i-1]
            if a != None and prices[i-1] > a and prices[i-1] > prices[i]:
                total += prices[i-1] - a
                a = None
            if a != None and prices[i] > a and i == len(prices) - 1:
                total += prices[i] - a
                a = None
        return total
    '''
    public class Solution {
    public int maxProfit(int[] prices) {
        int total = 0;
        for (int i=0; i< prices.length-1; i++) {
            if (prices[i+1]>prices[i]) total += prices[i+1]-prices[i];
        }
        
        return total;
    }
    '''

