class Ex121(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        cur = prices[0]
        t_max = 0
        for i in range(1, len(prices)):
            if cur < prices[i]:
                t = prices[i] - cur
                t_max = max(t_max, t)
            if prices[i] < cur:
                cur = prices[i]
        return t_max
    '''
    # Kadane's Algorithm
    public int maxProfit(int[] prices) {
        int maxCur = 0, maxSoFar = 0;
        for(int i = 1; i < prices.length; i++) {
            maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);
            maxSoFar = Math.max(maxCur, maxSoFar);
        }
        return maxSoFar;
    }
    '''
    '''
    result = 0
    min_value = prices[0]
    for i in xrange(1, len(prices)):
        result = max(result, prices[i] - min_value)
        min_value = min(min_value, prices[i])
    return result

    dp = [0] * len(prices)
    min_price = prices[0]
            
    for i in range(len(prices)):
        dp[i] = max(dp[i - 1], prices[i] - min_price)
        min_price = min(min_price, prices[i])
                
    return dp[-1]
    '''
    '''
    int min = Integer.MAX_VALUE;
    public int maxProfit(int[] prices) {
        return Arrays.stream(prices).map(i -> i - (min = Math.min(min, i))).max().orElse(0);
    }
    '''
    
ex121 = Ex121()
p = [7, 1, 5, 3, 6, 4]
p = [7, 6, 4, 3, 1]
print 121, ex121.maxProfit(p)

