class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        in_d = [0 for i in range(N)]
        out_d = [0 for i in range(N)]
        for a,b in trust:
            a -= 1; b -= 1
            out_d[a] += 1
            in_d[b] += 1
        for i in range(N):
            if in_d[i] == N-1 and out_d[i] == 0:
                return i+1
        return -1
