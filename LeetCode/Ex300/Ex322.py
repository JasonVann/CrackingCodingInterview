class Ex322(object):        
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Dic. O(mn)
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        if amount in coins:
            return 1

        coins.sort()
        # coins = coins[::-1]
        if amount < coins[0]:
            return -1
        A = {}
        for j in coins:
            A[j] = 1
        start = coins[0]
        for i in range(start, amount + 1):  
            if i not in A:
                continue
            for j in coins:                
                if i + j not in A or A[i+j] > A[i] + 1:
                    A[i + j] = A[i] + 1
        return -1 if amount not in A else A[amount]
           
    def coinChange0(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Array
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        if amount in coins:
            return 1

        coins.sort()
        # coins = coins[::-1]
        if amount < coins[0]:
            return -1
        A = [-1] * (coins[0] + 1)
        # A[0] = 0
        A[coins[0]] = 1
        start = coins[0] * 1

        for i in range(start + 1, amount + 1):
            temp = []

            for j in coins:
                if i % j == 0:
                    temp.append(i / j)
                if i < j:
                    break
                if A[i - j] != -1:
                    temp.append(A[i - j] + 1)
            cur = None
            if len(temp) > 0:
                cur = min(temp)
                # break
                A.append(cur)
            else:
                A.append(-1)
        # return A[3], A[2]
        # print A
        return A[-1]
    '''
    public class Solution {
        int total = Integer.MAX_VALUE;
        public int coinChange(int[] coins, int amount) {
            if (amount == 0) return 0;
            Arrays.sort(coins);
            count(amount, coins.length-1, coins, 0);
            return total == Integer.MAX_VALUE?-1:total;
        }
        void count(int amount, int index, int[] coins, int count){
            if (index<0 || count>=total-1) return;
            int c = amount/coins[index];
            for (int i = c;i>=0;i--){
                int newCount = count + i;
                int rem = amount - i*coins[index];
                
                if (rem>0 && newCount<total)
                    count(rem, index-1, coins, newCount);
                else if (newCount<total)
                    total = newCount;
                else if (newCount>=total-1)
                    break;
            }
        }
    }
    '''
    
ex322 = Ex322()
c = [1,2,5]
a = 11
c = [313,230,410,263,338,469,431,118,41,221]
a = 4906
c = [255,196,450,227,98,259,386,36,287,6]
a = 4063
a = [370,417,408,156,143,434,168,83,177,280,117]
a = 9953
c = [196,227,443,174,277,148]
a = 946
c = [1,2,5]
a = 10
c = [294,177,81,226,425,316,204,356,336,278,60]
a = 2267
c = [2]
a = 3
c = [176,6,366,357,484,226,1,104,160,331]
a = 5557
c = [370,417,408,156,143,434,168,83,177,280,117]
a = 9953
#c = [1,2147483647]
#a = 2
print 322, ex322.coinChange(c, a)

