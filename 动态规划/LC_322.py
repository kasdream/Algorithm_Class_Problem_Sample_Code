class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #边界条件
        if amount == 0: return 0
        if amount < min(coins): return -1
        if len(coins) == 0: return -1
        
        n = len(coins)
        import numpy as np
        
        #初始化
        #这里用numpy的数组会超时，改成了list，不过如果是面试的时候放心用，不会有这些问题
        inf = 1000000000
        dp = [0]
        dp += [inf for i in range(amount)]
        
        #状态转移方程
        for i in range(1,amount+1):
            for coin in coins:
                #这里注意判断合法
                if i >= coin:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        #判断结果
        if dp[amount] == inf:
            return -1
        return dp[amount]
