class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        #边界条件
        if n == 0 or m == 0: 
            return m+n
        
        
        import numpy as np
        #定义dp数组
        dp = np.zeros((n+1,m+1),dtype=np.int32)
        #初始化，除了dp[i][0]和dp[0][i],其余初始化为一个极大值
        dp.fill(1000000000)
        for i in range(n+1):
            dp[i][0] = i
        for i in range(m+1):
            dp[0][i] = i
            
        #状态转移方程
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j] = min( dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1), 
                              min(dp[i-1][j]+1,dp[i][j-1]+1))
        return dp[n][m]
