class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        
        #我们的下标是从0开始的，所以所有的点的index需要-1
        K -= 1
        
        #建图
        e = [[] for i in range(N)]
        for u,v,w in times:
            u -=1; v -=1
            e[u].append([v,w])
        
        #新建dis数组
        inf = 10000000
        dis = [inf for i in range(N)]
        dis[K] = 0
        
        #把源点相邻的点和距离放入堆中
        heap = []
        for v,w in e[K]:
            heapq.heappush(heap,(w,v))
            dis[v] = w
            
        #当堆不为空
        while not len(heap) == 0:
            #取出堆顶元素
            d,s = heapq.heappop(heap)
            #注意这里，下面有提到
            if dis[s] != d: continue
            for x,l in e[s]:
                if dis[x] > d + l:
                    #按照理论讲解，这里应该有一个出堆操作，
                    #但是实际上可以不实际出堆，而是插入一个距离更小的二元组
                    #这样在上面判断dis是否为最小值就可以跳过了
                    dis[x] = d + l
                    heapq.heappush(heap,(dis[x],x))
        #取距离最大值为答案
        ans = max(dis)
        if ans == inf: return -1
        return ans
